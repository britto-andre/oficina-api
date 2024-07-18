import uuid

from datetime import datetime
from typing import Annotated, Optional
from pydantic import BaseModel, BeforeValidator, Field

from src.app.common.str_util import camel_to_snake

PyObjectId = Annotated[str, BeforeValidator(str)]

class Event (BaseModel):
    id: Optional[PyObjectId] = Field(default=None)
    event_name: str
    aggregate_id: str
    aggregate_type: str
    payload: object
    created_time: datetime
    created_user: str

class EventBuilder:

    def build(self, payload_id, payload, event_name, user) -> Event:
        return Event(
            event_name=event_name,
            aggregate_id=str(payload_id),
            aggregate_type=camel_to_snake(payload.__class__.__name__),
            payload=payload.model_dump(by_alias=True, exclude=["id"]),
            created_time=datetime.now(),
            created_user=user,
        )