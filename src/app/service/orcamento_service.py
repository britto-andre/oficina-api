from src.app.entity.orcamento import Orcamento
from src.app.common.default_service import DefaultService
from src.app.repository.orcamento_repository import OrcamentoRepository
from src.app.repository.veiculo_repository import VeiculoRepository
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

        obj_id = self.repository.create(oficina_cod, obj)
        self.save_event(obj_id, obj, 'orcamento_criado', user, oficina_cod)
        return obj_id

    def list(self, oficina_cod):
        return self.repository.list(oficina_cod)
    
    def find_one_by_id(self, oficina_cod, id):
        orcamento =  self.repository.find_one_by_id(oficina_cod, id)
        # Carregar o veículo
        # Carregar o cliente
        # Carregar os itens
        return orcamento
    
# TO-DO: Add endpoints
# - Criar orçamento
# - Carregar orçamento - com todas as dependências
# - Atualizar itens do orçamento
# - Postergar validade
# - FInalizar orçamento
# - cancelar orçamento