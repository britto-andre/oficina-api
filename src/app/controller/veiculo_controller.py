from fastapi import APIRouter, Depends, Body, HTTPException, status
from pydantic import BaseModel
from typing import Annotated
from src.app.common.security_util import active_user
from src.app.service.veiculo_service import VeiculoService, ClienteNaoExisteException, PlacaCadastradaException
from src.app.entity.veiculo import Veiculo

router = APIRouter()
service = VeiculoService()

class VeiculoCriar(BaseModel):
    cliente_id: str
    placa: str
    marca: str
    modelo: str

class VeiculoTransferir(BaseModel): cliente_id: str

@router.post('/')
async def create(user: Annotated[dict, Depends(active_user)],
                 body: VeiculoCriar = Body(...)):
    try:
        obj = Veiculo(**body.model_dump())
        id = service.create(user['oficina'], user['email'], obj)
        return {'message': 'Veículo Criado', '_id': str(id)}
    except ClienteNaoExisteException:
        raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST, detail={'message': 'Cliente não existe.'})
    except PlacaCadastradaException:
        raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST, detail={'message': 'Placa já foi cadastrada.'})

@router.get('/')
async def list(user: Annotated[dict, Depends(active_user)]):
    list = service.list(user['oficina'])
    return {'list': list}

@router.get('/cliente/{cliente_id}')
async def list_by_cliente(user: Annotated[dict, Depends(active_user)], cliente_id):
    return service.list_by_cliente(user['oficina'], cliente_id)

@router.post('/{id}/transferir')
async def alterar_nome(user: Annotated[dict, Depends(active_user)], id,
                 body: VeiculoTransferir = Body(...)):
    try:
        service.transferir(user['oficina'], user['email'], id, body.cliente_id)
        return {'message': 'Veículo Transferido', '_id': str(id)}
    except ClienteNaoExisteException:
        raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST, detail={'message': 'Cliente não existe.'})