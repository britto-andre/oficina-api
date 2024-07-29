from pydantic import Field
from src.app.common.deafult_entity import DefaultEntity
from src.app.entity.veiculo import Veiculo
from src.app.entity.peca import Peca
from src.app.entity.servico import Servico

class OrcamentoItem (DefaultEntity):
    tipo: str
    tipo_id: str
    valor: float
    peca: Peca = Field(default=None)
    servico: Servico = Field(default=None)

class Orcamento (DefaultEntity):
    veiculo_id: str
    veiculo: Veiculo = Field(default=None)
    observacao: str
    condicao_pgto: str
    telefone_cliente: str
    validade_dias: int
    situacao: str
    itens: list

    # TO-DO Médito para calcular o valor total do orçamento
