from pydantic import BaseModel, Field
from src.app.common.deafult_entity import DefaultEntity
from src.app.entity.veiculo import Veiculo
from src.app.entity.peca import Peca
from src.app.entity.servico import Servico

class OrcamentoItem (BaseModel):
    tipo: str
    tipo_id: str
    quantidade: float
    valor: float
    peca: object = Field(default=None)
    servico: object = Field(default=None)

class Orcamento (DefaultEntity):
    veiculo_id: str
    veiculo: object = Field(default=None)
    cliente: object = Field(default=None)
    observacao: str
    condicao_pgto: str
    telefone_cliente: str
    validade_dias: int
    situacao: str = Field(default=None)
    itens: list

    # TO-DO Médito para calcular o valor total do orçamento
