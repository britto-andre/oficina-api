from src.app.entity.peca import Peca
from src.app.common.default_service import DefaultService
from src.app.repository.peca_repository import PecaRepository

class PecaService(DefaultService):

    def __init__(self) -> None:
        super().__init__()
        self.repository = PecaRepository()

    def create(self, oficina_cod, user, obj: Peca):
        obj_id = self.repository.create(oficina_cod, obj)
        self.save_event(obj_id, obj, 'peca_criada', user, oficina_cod)
        return obj_id

    def list(self, oficina_cod):
        return self.repository.list(oficina_cod)
    
    # TO-DO: 
    #   - Atualizar nome da peça
    #   - Atualizar a margem de lucro
    #   - Atualizar o prazo entrega
    #   - Atualizar o custo da peca