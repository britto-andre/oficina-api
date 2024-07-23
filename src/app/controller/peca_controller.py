from fastapi import APIRouter, Depends, Body
from pydantic import BaseModel
from typing import Annotated
from src.app.common.security_util import active_user
from src.app.service.peca_service import PecaService
from src.app.entity.peca import Peca

router = APIRouter()
service = PecaService()

class PecaCreate(BaseModel):
    nome: str
    prazo_medio_entrega: str
    custo: float
    margem_lucro: float

@router.post('/')
async def create(user: Annotated[dict, Depends(active_user)],
                 body: PecaCreate = Body(...)):
    obj = Peca(**body.model_dump())
    id = service.create(user['oficina'], user['email'], obj)
    return {'message': 'Peça Criada', '_id': str(id)}

@router.get('/')
async def list(user: Annotated[dict, Depends(active_user)]):
    list = service.list(user['oficina'])
    return {'list': list}

    
    # TO-DO:
    #   - Cadastro da peca
    #   - Atualizar nome da peça
    #   - Atualizar a margem de lucro
    #   - Atualizar o prazo entrega
    #   - Atualizar o custo da peca