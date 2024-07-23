from fastapi import APIRouter, Depends
from typing import Annotated
from src.app.common.security_util import active_user

router = APIRouter()

@router.get('/')
async def list(user: Annotated[dict, Depends(active_user)]):
    return {'list': []}