from pydantic import Field
from src.app.common.deafult_entity import DefaultEntity

class Oficina (DefaultEntity):
    nome: str
    email: str
    codigo: str = Field(default=None)