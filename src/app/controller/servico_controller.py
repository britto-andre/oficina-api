from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel
from src.app.service.servico_service import ServicoService
from src.app.entity.servico import Servico

# from fastapi_keycloak_middleware import get_user

router = APIRouter()
service = ServicoService()

class ServicoCreate(BaseModel):
    nome: str
    valor: float

@router.post('/')
async def create(body: ServicoCreate = Body(...)):
    obj = Servico(**body.model_dump())
    id = service.create(obj)
    return {'message': 'Servico Criado', '_id': str(id)}

@router.get('/{id}')
async def find_on_by_id(id):
    return service.find_one_by_id(id)

@router.get('/')
async def list():
    list = service.list()
    return {'list': list}

# @router.delete('/{id}')
# async def delete(id):
#     result = service.request_delete(id)
#     if not result:
#         raise HTTPException(status_code= 404, detail= {'message': 'Example not found', '_id': id})
#     return {'message': 'Delete requested', '_id': id}