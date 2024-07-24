from src.app.entity.peca import Peca
from src.app.common.default_repository import DefaultRepository

class PecaRepository(DefaultRepository):

    def __init__(self):
        super().__init__()
        self._collection = 'peca'

    def create(self, oficina_cod, obj: Peca):
        inserted_id = super().create(f'{oficina_cod}_{self._collection}', obj)
        return inserted_id
    
    def update(self, oficina_cod, id, payload):
        super().update(f'{oficina_cod}_{self._collection}', id, payload)
    
    def list(self, oficina_cod):
        results = super().list(f'{oficina_cod}_{self._collection}')
        return list(map(lambda r: Peca(**r.to_dict()), results))