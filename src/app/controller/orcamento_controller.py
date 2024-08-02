from fastapi import APIRouter, Depends, Body, HTTPException, status
from pydantic import BaseModel
from typing import Annotated
from src.app.common.security_util import active_user
from src.app.service.orcamento_service import OrcamentoService, VeiculoNaoExisteException, ServicoNaoExisteException, PecaNaoExisteException, ItensVazioException
from src.app.entity.orcamento import Orcamento, OrcamentoItem

router = APIRouter()
service = OrcamentoService()

class OrcamentoCriar(BaseModel):
    veiculo_id: str
    observacao: str
    condicao_pgto: str
    telefone_cliente: str
    validade_dias: int
    itens: list

class OrcamentoItemAtualizar(BaseModel): itens: list
class OrcamentoPostergar(BaseModel): validade_dias: int

@router.post('/')
async def create(user: Annotated[dict, Depends(active_user)],
                 body: OrcamentoCriar = Body(...)):
    try:
        obj = Orcamento(**body.model_dump())
        itens = []
        for item in body.itens:
            itens.append(OrcamentoItem(**item))
        obj.itens = itens
        id = service.create(user['oficina'], user['email'], obj)
        return {'message': 'Orçamento Criado', '_id': str(id)}
    except VeiculoNaoExisteException:
        raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST, detail={'message': 'Veículo não existe.'})
    except ServicoNaoExisteException:
        raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST, detail={'message': 'Serviço não existe.'})
    except PecaNaoExisteException:
        raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST, detail={'message': 'Peça não existe.'})
    except ItensVazioException:
        raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST, detail={'message': 'Orçamento não possui itens.'})

@router.get('/')
async def list(user: Annotated[dict, Depends(active_user)]):
    list = service.list(user['oficina'])
    return {'list': list}

@router.get('/{id}')
async def find_on_by_id(user: Annotated[dict, Depends(active_user)], id):
    return service.find_one_by_id(user['oficina'], id)

@router.post('/{id}/atualizar_itens')
async def update_itens(user: Annotated[dict, Depends(active_user)], id,
                 body: OrcamentoItemAtualizar = Body(...)):
    try:
        itens = []
        for item in body.itens:
            itens.append(OrcamentoItem(**item))
        service.atualizar_itens(user['oficina'], user['email'], id, itens)
        return {'message': 'Itens do Orçamento Atualizados', '_id': str(id)}
    except ServicoNaoExisteException:
        raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST, detail={'message': 'Serviço não existe.'})
    except PecaNaoExisteException:
        raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST, detail={'message': 'Peça não existe.'})
    except ItensVazioException:
        raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST, detail={'message': 'Lista de itens não pode ser vazia.'})

@router.post('/{id}/postergar')
async def postergar(user: Annotated[dict, Depends(active_user)], id,
                 body: OrcamentoPostergar = Body(...)):
    service.postergar(user['oficina'], user['email'], id, body.validade_dias)
    return {'message': 'Orçamento Postergado', '_id': str(id)}

@router.post('/{id}/cancelar')
async def cancelar(user: Annotated[dict, Depends(active_user)], id):
    service.cancelar(user['oficina'], user['email'], id)
    return {'message': 'Orçamento Cancelado', '_id': str(id)}

@router.post('/{id}/finalizar')
async def finalizar(user: Annotated[dict, Depends(active_user)], id):
    service.finalizar(user['oficina'], user['email'], id)
    return {'message': 'Orçamento Cancelado', '_id': str(id)}