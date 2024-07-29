from src.app.entity.veiculo import Veiculo
from src.app.common.default_service import DefaultService
from src.app.repository.veiculo_repository import VeiculoRepository
from src.app.repository.cliente_repository import ClienteRepository

class ClienteNaoExisteException(Exception): pass
class PlacaCadastradaException(Exception): pass

class VeiculoService(DefaultService):

    def __init__(self) -> None:
        super().__init__()
        self.repository = VeiculoRepository()
        self.cliente_repository = ClienteRepository()
    
    def _checkPlacaCadastrada(self, oficina_cod, placa):
        veiculo = self.repository.find_one_by_placa(oficina_cod, placa)
        if veiculo: raise PlacaCadastradaException()

    def _checkClienteExiste(self, oficina_cod, id):
        cliente = self.cliente_repository.find_one_by_id(oficina_cod, id)
        if not cliente: raise ClienteNaoExisteException()

    def create(self, oficina_cod, user, obj: Veiculo):
        self._checkClienteExiste(oficina_cod, obj.cliente_id)
        self._checkPlacaCadastrada(oficina_cod, obj.placa)
        obj_id = self.repository.create(oficina_cod, obj)
        self.save_event(obj_id, obj, 'veiculo_criado', user, oficina_cod)
        return obj_id

    def list(self, oficina_cod):
        return self.repository.list(oficina_cod)
    
    def list_by_cliente(self, oficina_cod, cliente_id):
        return self.repository.list_by_cliente(oficina_cod, cliente_id)
    
    def transferir(self, oficina_cod, user, id, cliente_id):
        self._checkClienteExiste(oficina_cod, cliente_id)
        payload = {'cliente_id': cliente_id}
        self.repository.update(oficina_cod, id, payload)
        self.save_event_classname(id, Veiculo.__name__, payload, 'veiculo_transferido', user, oficina_cod)