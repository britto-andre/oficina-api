from src.app.entity.servico import Servico
from src.app.common.default_repository import DefaultRepository

class ServicoRepository(DefaultRepository):

    def __init__(self):
        super().__init__()
        self._collection = 'servico'

    def create(self, oficina_cod, obj: Servico):
        inserted_id = super().create(f'{oficina_cod}_{self._collection}', obj)
        return inserted_id
    
    def update(self, oficina_cod, id, payload):
        super().update(f'{oficina_cod}_{self._collection}', id, payload)
    
    def list(self, oficina_cod):
        results = super().list(f'{oficina_cod}_{self._collection}')
        return list(map(lambda r: Servico(**r.to_dict()), results))
    
    def find_one_by_id(self, oficina_cod, codigo):
        result = super().findOne(f'{oficina_cod}_{self._collection}', codigo)
        return Servico(**result.to_dict())