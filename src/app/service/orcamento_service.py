from src.app.entity.orcamento import Orcamento
from src.app.common.default_service import DefaultService
from src.app.repository.orcamento_repository import OrcamentoRepository

class VeiculoNaoExisteException(Exception): pass
class ServicoNaoExisteException(Exception): pass
class PecaNaoExisteException(Exception): pass

class OrcamentoService(DefaultService):

    def __init__(self) -> None:
        super().__init__()
        self.repository = OrcamentoRepository()
        # self.cliente_repository = ClienteRepository()
    
    # def _checkClienteExiste(self, oficina_cod, id):
    #     cliente = self.cliente_repository.find_one_by_id(oficina_cod, id)
    #     if not cliente: raise ClienteNaoExisteException()

    def create(self, oficina_cod, user, obj: Orcamento):
        # todo - checar se o veículo existe
        # todo - iterar sobre os itens para validar se a peça ou o serviço existem
        # self._checkClienteExiste(oficina_cod, obj.cliente_id)
        obj_id = self.repository.create(oficina_cod, obj)
        self.save_event(obj_id, obj, 'orcamento_criado', user, oficina_cod)
        return obj_id

    def list(self, oficina_cod):
        return self.repository.list(oficina_cod)