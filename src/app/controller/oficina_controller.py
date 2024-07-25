from fastapi import APIRouter, Depends, Body, HTTPException, status
from typing import Annotated
from pydantic import BaseModel
from src.app.common.security_util import active_user_only
from src.app.service.oficina_service import OficinaService
from src.app.entity.oficina import Oficina

router = APIRouter()
service = OficinaService()

class OficinaCreate(BaseModel):
    nome: str

@router.post('/')
async def create(user: Annotated[dict, Depends(active_user_only)], 
                 body: OficinaCreate = Body(...)):
    obj = Oficina(**{'nome':body.nome, 'email':user['email']})
    id = service.create(obj, user['email'])
    if not id: 
        raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST,
           detail={'message': 'Usuário já possui oficina cadastrada.'})
    
    return {'message': 'Oficina Criada', '_id': str(id)}

@router.get('/')
async def find(user: Annotated[dict, Depends(active_user_only)]):
    obj = service.find_one_by_email(user['email'])
    return {'data': obj}