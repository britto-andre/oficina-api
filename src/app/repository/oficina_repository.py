from src.app.entity.oficina import Oficina
from src.app.common.default_repository import DefaultRepository

class OficinaRepository(DefaultRepository):

    def __init__(self):
        super().__init__()
        self._collection = 'oficina'
    
    def _return_one(self, result:list):
        if not result: return None
        return Oficina(**result[0].to_dict())

    def create(self, obj: Oficina):
        inserted_id = super().create(self._collection, obj)
        return inserted_id
        
    def find_one_by_email(self, email):
        result = super().find(self._collection, 'email','==', email)
        return self._return_one(result)
    
    def find_one_by_codigo(self, codigo):
        result = super().find(self._collection, 'codigo','==', codigo)
        return self._return_one(result)