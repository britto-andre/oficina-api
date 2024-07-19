from src.app.common.event import Event
from src.app.common.default_repository import DefaultRepository
from google.cloud.firestore_v1.base_query import FieldFilter

class EventRepository(DefaultRepository):

    def __init__(self):
        super().__init__()
        self._collection = 'events'

    def create(self, obj: Event, collection_previx):
        inserted_id = super().create(f'{collection_previx}_{self._collection}', obj)
        return inserted_id
    
    def list_by_aggregate(self, collection_previx: str, aggregate_type: str, aggregate_id: str):
        query = self.db.collection(f'{collection_previx}_{self._collection}')
        query = query.where(filter=FieldFilter('aggregate_type', '==', aggregate_type))
        query = query.where(filter=FieldFilter('aggregate_id', '==', aggregate_id))
        results = query.get()
        return list(map(lambda r: Event(**r.to_dict()), results))
