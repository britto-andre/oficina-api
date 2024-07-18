from pydantic import Field
from src.app.common.deafult_entity import DefaultEntity
from src.app.common.str_util import normalize

class Oficina (DefaultEntity):
    nome: str
    email: str
    codigo: str = Field(default=None)