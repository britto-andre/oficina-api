from src.app.entity.orcamento import Orcamento
from src.app.common.default_service import DefaultService
from src.app.repository.orcamento_repository import OrcamentoRepository
from src.app.repository.veiculo_repository import VeiculoRepository
from src.app.repository.cliente_repository import ClienteRepository
from src.app.repository.peca_repository import PecaRepository
from src.app.repository.servico_repository import ServicoRepository

class VeiculoNaoExisteException(Exception): pass
class ItensVazioException(Exception): pass
class ServicoNaoExisteException(Exception): pass
class PecaNaoExisteException(Exception): pass

class OrcamentoService(DefaultService):

    def __init__(self) -> None:
        super().__init__()
        self.repository = OrcamentoRepository()
        self.veiculo_repository = VeiculoRepository()
        self.cliente_repository = ClienteRepository()
        self.peca_repository = PecaRepository()
        self.servico_repository = ServicoRepository()
    
    def _checkVeiculoExiste(self, oficina_cod, id):
        veiculo = self.veiculo_repository.find_one_by_id(oficina_cod, id)
        if not veiculo: raise VeiculoNaoExisteException()

    def _checkItensExiste(self, oficina_cod, itens: list):
        if itens is None or not itens:
            raise ItensVazioException()

        for item in itens:
            if item.tipo == 'peca':
                peca = self.peca_repository.find_one_by_id(oficina_cod, item.tipo_id)
                if not peca: raise PecaNaoExisteException()
            else:
                servico = self.servico_repository.find_one_by_id(oficina_cod, item.tipo_id)
                if not servico: raise ServicoNaoExisteException()

    def create(self, oficina_cod, user, obj: Orcamento):
        self._checkVeiculoExiste(oficina_cod, obj.veiculo_id)
        self._checkItensExiste(oficina_cod, obj.itens)
        obj.situacao = 'novo'
        obj_id = self.repository.create(oficina_cod, obj)
        self.save_event(obj_id, obj, 'orcamento_criado', user, oficina_cod)
        return obj_id

    def list(self, oficina_cod):
        return self.repository.list(oficina_cod)
    
    def find_one_by_id(self, oficina_cod, id):
        orcamento =  self.repository.find_one_by_id(oficina_cod, id)
        if orcamento:
            orcamento.veiculo = self.veiculo_repository.find_one_by_id(oficina_cod, orcamento.veiculo_id)
            orcamento.cliente = self.cliente_repository.find_one_by_id(oficina_cod, orcamento.veiculo.cliente_id)

            for item in orcamento.itens:
                if item['tipo'] == 'peca':
                    item['peca'] = self.peca_repository.find_one_by_id(oficina_cod, item['tipo_id'])
                else:
                    item['servico'] = self.servico_repository.find_one_by_id(oficina_cod, item['tipo_id'])

        return orcamento
    
    def atualizar_itens(self, oficina_cod, user, id, itens):
        self._checkItensExiste(oficina_cod, itens)
        payload = {"itens": list(map(lambda r: r.model_dump(), itens)), "situacao": "atualizado"}
        self.repository.update(oficina_cod, id, payload)
        self.save_event_classname(id, Orcamento.__name__, payload, 'orcamento_itens_atualizado', user, oficina_cod)
    
    def postergar(self, oficina_cod, user, id, validade_dias):
        payload = {"validade_dias": validade_dias, "situacao": "atualizado"}
        self.repository.update(oficina_cod, id, payload)
        self.save_event_classname(id, Orcamento.__name__, payload, 'orcamento_postergado', user, oficina_cod)
    
    def cancelar(self, oficina_cod, user, id):
        payload = {"situacao": "cancelado"}
        self.repository.update(oficina_cod, id, payload)
        self.save_event_classname(id, Orcamento.__name__, payload, 'orcamento_cancelado', user, oficina_cod)

    def finalizar(self, oficina_cod, user, id):
        payload = {"situacao": "finalizado"}
        self.repository.update(oficina_cod, id, payload)
        self.save_event_classname(id, Orcamento.__name__, payload, 'orcamento_finalizado', user, oficina_cod)