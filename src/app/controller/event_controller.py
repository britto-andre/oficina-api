from fastapi import APIRouter, Depends
from typing import Annotated
from src.app.common.security_util import active_user
from src.app.service.event_service import EventService

router = APIRouter()
service = EventService()

@router.get('/{oficina}/{aggregate_type}/{aggregate_id}')
async def list_by_aggregate(oficina:str, aggregate_type: str, aggregate_id: str):
        list = service.list_by_aggregate(oficina, aggregate_type, aggregate_id)
        return {'list': list}