from src.app.entity.cliente import Cliente
from src.app.common.default_repository import DefaultRepository

class ClienteRepository(DefaultRepository):

    def __init__(self):
        super().__init__()
        self._collection = 'cliente'

    def create(self, oficina_cod, obj: Cliente):
        inserted_id = super().create(f'{oficina_cod}_{self._collection}', obj)
        return inserted_id
    
    def update(self, oficina_cod, id, payload):
        super().update(f'{oficina_cod}_{self._collection}', id, payload)
    
    def list(self, oficina_cod):
        results = super().list(f'{oficina_cod}_{self._collection}')
        return list(map(lambda r: Cliente(**r.to_dict()), results))
    
    def find_one_by_telefone(self, oficina_cod, telefone):
        result = super().find(f'{oficina_cod}_{self._collection}', 'telefone','==', telefone)
        if not result: return None
        return Cliente(**result[0].to_dict())