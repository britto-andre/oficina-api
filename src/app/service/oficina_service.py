from src.app.common.logger import logger
# from src.app.common.service.default_service import DefaultService
from src.app.entity.oficina import Oficina
from src.app.repository.oficina_repository import OficinaRepository

class OficinaService():

    def __init__(self) -> None:
        # super().__init__()
        self.repository = OficinaRepository()

    def create(self, obj: Oficina):
        oficina = self.repository.find_one_by_email(obj.email)
        if not oficina:
            obj_id = self.repository.create(obj)
            return obj_id
        else:
            return None
    
    def find_one_by_email(self, email):
        return self.repository.find_one_by_email(email)

    # def update_name(self, id: str, name: str):
    #     logger.info(f'update_name -> id: {id}, name: {name}')

    
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