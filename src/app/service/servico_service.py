from src.app.entity.servico import Servico
from src.app.common.default_service import DefaultService
from src.app.repository.servico_repository import ServicoRepository

class ServicoService(DefaultService):

    def __init__(self) -> None:
        super().__init__()
        self.repository = ServicoRepository()

    def create(self, oficina_cod, user, obj: Servico):
        obj_id = self.repository.create(oficina_cod, obj)
        self.save_event(obj_id, obj, 'servico_criado', user, oficina_cod)
        return obj_id

    def list(self, oficina_cod):
        return self.repository.list(oficina_cod)
    
    def find_one_by_id(self, oficina_cod, id):
        return self.repository.find_one_by_id(oficina_cod, id)
    
    # def request_delete(self, id: str):
    #     obj = self.repository.find_one_by_id(id)
    #     if obj:
    #         self.publisher.publish(id, obj, 'example_delete_requested')
    #         return True
    #     return False

    # def delete(self, id: str):
    #     obj = self.repository.find_one_by_id(id)
    #     if obj:
    #         self.repository.delete(obj)
    #         return True
    #     return False