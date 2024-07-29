from fastapi import APIRouter, Depends, Body, HTTPException, status
from pydantic import BaseModel
from typing import Annotated
from src.app.common.security_util import active_user
from src.app.service.orcamento_service import OrcamentoService, VeiculoNaoExisteException, ServicoNaoExisteException, PecaNaoExisteException
from src.app.entity.orcamento import Orcamento

router = APIRouter()
service = OrcamentoService()

class OrcamentoCriar(BaseModel):
    veiculo_id: str
    observacao: str
    condicao_pgto: str
    telefone_cliente: str
    validade_dias: int
    itens: list

class OrcamentoItemAtualizar(BaseModel):
    tipo: str
    tipo_id: str
    valor: float

@router.post('/')
async def create(user: Annotated[dict, Depends(active_user)],
                 body: OrcamentoCriar = Body(...)):
    try:
        obj = Orcamento(**body.model_dump())
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

@router.get('/')
async def list(user: Annotated[dict, Depends(active_user)]):
    list = service.list(user['oficina'])
    return {'list': list}

# TO-DO: Add endpoints
# - Criar orçamento
# - Carregar orçamento
# - Atualizar itens do orçamento
# - Postergar validade
# - FInalizar orçamento
# - cancelar orçamento