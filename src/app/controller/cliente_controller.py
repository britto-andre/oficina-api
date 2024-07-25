from fastapi import APIRouter, Depends, Body, HTTPException, status
from pydantic import BaseModel
from typing import Annotated
from src.app.common.security_util import active_user
from src.app.service.cliente_service import ClienteService, TelefoneEmUsoException
from src.app.entity.cliente import Cliente

router = APIRouter()
service = ClienteService()

class ClienteCriar(BaseModel):
    nome: str
    telefone: str

class ClienteAlterarNome(BaseModel): nome: str
class ClienteAlterarTelefone(BaseModel): telefone: str

@router.post('/')
async def create(user: Annotated[dict, Depends(active_user)],
                 body: ClienteCriar = Body(...)):
    try:
        obj = Cliente(**body.model_dump())
        id = service.create(user['oficina'], user['email'], obj)
        return {'message': 'Cliente Criado', '_id': str(id)}
    except TelefoneEmUsoException:
        raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST,
           detail={'message': 'Telefone em uso.'})

@router.get('/')
async def list(user: Annotated[dict, Depends(active_user)]):
    list = service.list(user['oficina'])
    return {'list': list}

@router.get('/telefone/{telefone}')
async def find_on_by_id(user: Annotated[dict, Depends(active_user)], telefone):
    return service.find_one_by_telefone(user['oficina'], telefone)

@router.post('/{id}/alterar_nome')
async def alterar_nome(user: Annotated[dict, Depends(active_user)], id,
                 body: ClienteAlterarNome = Body(...)):
    service.alterar_nome(user['oficina'], user['email'], id, body.nome)
    return {'message': 'Nome do Cliente Atualizado', '_id': str(id)}

@router.post('/{id}/alterar_telefone')
async def alterar_telefone(user: Annotated[dict, Depends(active_user)], id,
                 body: ClienteAlterarTelefone = Body(...)):
    try:
        service.alterar_telefone(user['oficina'], user['email'], id, body.telefone)
        return {'message': 'Telefone do Cliente Atualizado', '_id': str(id)}
    except TelefoneEmUsoException: 
        raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST,
           detail={'message': 'Telefone em uso.'})