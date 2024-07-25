import re
from src.app.entity.cliente import Cliente
from src.app.common.default_service import DefaultService
from src.app.repository.cliente_repository import ClienteRepository

class TelefoneEmUsoException(Exception): pass

class ClienteService(DefaultService):

    def __init__(self) -> None:
        super().__init__()
        self.repository = ClienteRepository()
    
    def _checkTelefoneEmUso(self, oficina_cod, telefone):
        cliente = self.repository.find_one_by_telefone(oficina_cod, telefone)
        if cliente: raise TelefoneEmUsoException()

    def create(self, oficina_cod, user, obj: Cliente):
        obj.telefone = re.sub('[^0-9]', '', obj.telefone)
        self._checkTelefoneEmUso(oficina_cod, obj.telefone)
        obj_id = self.repository.create(oficina_cod, obj)
        self.save_event(obj_id, obj, 'cliente_criado', user, oficina_cod)
        return obj_id
    
    def find_one_by_telefone(self, oficina_cod, telefone):
        telefone = re.sub('[^0-9]', '', telefone)
        return self.repository.find_one_by_telefone(oficina_cod, telefone)

    def list(self, oficina_cod):
        return self.repository.list(oficina_cod)
    
    def alterar_nome(self, oficina_cod, user, id, nome):
        payload = {'nome': nome}
        self.repository.update(oficina_cod, id, payload)
        self.save_event_classname(id, Cliente.__name__, payload, 'cliente_nome_atualizado', user, oficina_cod)
    
    def alterar_telefone(self, oficina_cod, user, id, telefone):
        telefone = re.sub('[^0-9]', '', telefone)
        self._checkTelefoneEmUso(oficina_cod, telefone)
        payload = {'telefone': telefone}
        self.repository.update(oficina_cod, id, payload)
        self.save_event_classname(id, Cliente.__name__, payload, 'cliente_telefone_atualizado', user, oficina_cod)