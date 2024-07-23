from src.app.common.deafult_entity import DefaultEntity

class Peca (DefaultEntity):
    nome: str
    prazo_medio_entrega: str
    custo: float
    margem_lucro: float #percentual acrescido no custo no momento do orçamento