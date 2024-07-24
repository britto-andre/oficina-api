from fastapi import APIRouter, Depends, Body
from pydantic import BaseModel
from typing import Annotated
from src.app.common.security_util import active_user
from src.app.service.peca_service import PecaService
from src.app.entity.peca import Peca

router = APIRouter()
service = PecaService()

class PecaCriar(BaseModel):
    nome: str
    prazo_medio_entrega: str
    custo: float
    margem_lucro: float

class PecaAlterarNome(BaseModel): nome: str
class PecaAlterarPrazo(BaseModel): prazo_medio_entrega: str
class PecaAlterarCusto(BaseModel): custo: float
class PecaAlterarMargem(BaseModel): margem_lucro: float

@router.post('/')
async def create(user: Annotated[dict, Depends(active_user)],
                 body: PecaCriar = Body(...)):
    obj = Peca(**body.model_dump())
    id = service.create(user['oficina'], user['email'], obj)
    return {'message': 'Peça Criada', '_id': str(id)}

@router.get('/')
async def list(user: Annotated[dict, Depends(active_user)]):
    list = service.list(user['oficina'])
    return {'list': list}

@router.post('/{id}/alterar_nome')
async def alterar_nome(user: Annotated[dict, Depends(active_user)], id,
                 body: PecaAlterarNome = Body(...)):
    service.alterar_nome(user['oficina'], user['email'], id, body.nome)
    return {'message': 'Nome da Peça Atualizado', '_id': str(id)}

@router.post('/{id}/alterar_prazo')
async def alterar_prazo(user: Annotated[dict, Depends(active_user)], id,
                 body: PecaAlterarPrazo = Body(...)):
    service.alterar_prazo(user['oficina'], user['email'], id, body.prazo_medio_entrega)
    return {'message': 'Prazo Médio de Entrega da Peça Atualizado', '_id': str(id)}

@router.post('/{id}/alterar_custo')
async def alterar_custo(user: Annotated[dict, Depends(active_user)], id,
                 body: PecaAlterarCusto = Body(...)):
    service.alterar_custo(user['oficina'], user['email'], id, body.custo)
    return {'message': 'Custo da Peça Atualizado', '_id': str(id)}

@router.post('/{id}/alterar_margem')
async def alterar_margem(user: Annotated[dict, Depends(active_user)], id,
                 body: PecaAlterarMargem = Body(...)):
    service.alterar_margem(user['oficina'], user['email'], id, body.margem_lucro)
    return {'message': 'Margem de Lucro da Peça Atualizado', '_id': str(id)}