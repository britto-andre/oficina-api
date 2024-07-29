from src.app.entity.orcamento import Orcamento
from src.app.common.default_repository import DefaultRepository

class OrcamentoRepository(DefaultRepository):

    def __init__(self):
        super().__init__()
        self._collection = 'orcamento'

    def create(self, oficina_cod, obj: Orcamento):
        inserted_id = super().create(f'{oficina_cod}_{self._collection}', obj)
        return inserted_id
    
    def update(self, oficina_cod, id, payload):
        super().update(f'{oficina_cod}_{self._collection}', id, payload)
    
    def list(self, oficina_cod):
        results = super().list(f'{oficina_cod}_{self._collection}')
        return list(map(lambda r: Orcamento(**r.to_dict()), results))