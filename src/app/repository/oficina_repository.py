from src.app.entity.oficina import Oficina
from src.app.common.default_repository import DefaultRepository

class OficinaRepository(DefaultRepository):

    def __init__(self):
        super().__init__()
        self._collection = 'oficina'

    def create(self, obj: Oficina):
        inserted_id = super().create(self._collection, obj)
        return inserted_id
        
    def find_one_by_email(self, email):
        result = super().find(self._collection, 'email','==', email)
        if not result: return None
        print(result[0].to_dict())
        return Oficina(**result[0].to_dict())