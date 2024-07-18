from src.app.common.event import EventBuilder
from src.app.common.event_repository import EventRepository

class DefaultService:

    def __init__(self):
        self.event_repository = EventRepository()

    def save_event(self, payload_id, payload, event_name, user, collection_prefix):
        event = EventBuilder().build(payload_id = payload_id,
                                     payload = payload,
                                     event_name = event_name,
                                     user = user)
        
        self.event_repository.create(event, collection_prefix)
        
        