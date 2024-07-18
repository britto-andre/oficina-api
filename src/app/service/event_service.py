from src.app.common.event import Event
from src.app.common.event_repository import EventRepository

class EventService():

    def __init__(self) -> None:
        super().__init__()
        self.repository = EventRepository()

    def list_by_aggregate(self, oficina_cod: str, aggregate_type: str, aggregate_id: str):
        return self.repository.list_by_aggregate(oficina_cod, aggregate_type, aggregate_id)