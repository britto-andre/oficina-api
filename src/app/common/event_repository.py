from src.app.common.event import Event
from src.app.common.default_repository import DefaultRepository

class EventRepository(DefaultRepository):

    def __init__(self):
        super().__init__()
        self._collection = 'events'

    def create(self, obj: Event, collection_previx):
        inserted_id = super().create(f'{collection_previx}_{self._collection}', obj)
        return inserted_id