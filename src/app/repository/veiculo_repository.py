from src.app.entity.veiculo import Veiculo
from src.app.common.default_repository import DefaultRepository

class VeiculoRepository(DefaultRepository):

    def __init__(self):
        super().__init__()
        self._collection = 'veiculo'

    def create(self, oficina_cod, obj: Veiculo):
        inserted_id = super().create(f'{oficina_cod}_{self._collection}', obj)
        return inserted_id
    
    def update(self, oficina_cod, id, payload):
        super().update(f'{oficina_cod}_{self._collection}', id, payload)
    
    def list(self, oficina_cod):
        results = super().list(f'{oficina_cod}_{self._collection}')
        return list(map(lambda r: Veiculo(**r.to_dict()), results))
    
    def list_by_cliente(self, oficina_cod, cliente_id):
        results = super().find(f'{oficina_cod}_{self._collection}', 'cliente_id','==', cliente_id)
        return list(map(lambda r: Veiculo(**r.to_dict()), results))
    
    def find_one_by_placa(self, oficina_cod, placa):
        result = super().find(f'{oficina_cod}_{self._collection}', 'placa','==', placa)
        if not result: return None
        return Veiculo(**result[0].to_dict())
    
    def find_one_by_id(self, oficina_cod, id):
        result = super().findOne(f'{oficina_cod}_{self._collection}', id)
        if not result.to_dict(): return None
        return Veiculo(**result.to_dict())