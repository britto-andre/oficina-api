from fastapi import APIRouter, Depends
from typing import Annotated
from src.app.common.security_util import active_user
from src.app.service.event_service import EventService

router = APIRouter()
service = EventService()

@router.get('/{aggregate_type}/{aggregate_id}')
async def list_by_aggregate(aggregate_type: str, aggregate_id: str, user: Annotated[dict, Depends(active_user)]):
        list = service.list_by_aggregate(user['oficina'], aggregate_type, aggregate_id)
        return {'list': list}