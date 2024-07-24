from fastapi import APIRouter, Depends, Body
from pydantic import BaseModel
from typing import Annotated
from src.app.common.security_util import active_user
from src.app.service.servico_service import ServicoService
from src.app.entity.servico import Servico

router = APIRouter()
service = ServicoService()

class ServicoCriar(BaseModel):
    nome: str
    valor: float

class ServicoAlterarNome(BaseModel):
    nome: str

class ServicoAlterarValor(BaseModel):
    valor: float

@router.post('/')
async def create(user: Annotated[dict, Depends(active_user)],
                 body: ServicoCriar = Body(...)):
    obj = Servico(**body.model_dump())
    id = service.create(user['oficina'], user['email'], obj)
    return {'message': 'Serviço Criado', '_id': str(id)}

@router.post('/{id}/alterar_nome')
async def alterar_nome(user: Annotated[dict, Depends(active_user)], id,
                 body: ServicoAlterarNome = Body(...)):
    service.alterar_nome(user['oficina'], user['email'], id, body.nome)
    return {'message': 'Nome do Serviço Atualizado', '_id': str(id)}

@router.post('/{id}/alterar_valor')
async def alterar_valor(user: Annotated[dict, Depends(active_user)], id,
                 body: ServicoAlterarValor = Body(...)):
    service.alterar_valor(user['oficina'], user['email'], id, body.valor)
    return {'message': 'Valor do Serviço Atualizado', '_id': str(id)}

@router.get('/{id}')
async def find_on_by_id(user: Annotated[dict, Depends(active_user)], id):
    return service.find_one_by_id(user['oficina'], id)

@router.get('/')
async def list(user: Annotated[dict, Depends(active_user)]):
    list = service.list(user['oficina'])
    return {'list': list}

# @router.delete('/{id}')
# async def delete(id):
#     result = service.request_delete(id)
#     if not result:
#         raise HTTPException(status_code= 404, detail= {'message': 'Example not found', '_id': id})
#     return {'message': 'Delete requested', '_id': id}