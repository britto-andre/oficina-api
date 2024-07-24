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
    
    def alterar_nome(self, oficina_cod, user, id, nome):
        payload = {"nome": nome}
        self.repository.update(oficina_cod, id, payload)
        self.save_event_classname(id, Peca.__name__, payload, 'peca_nome_atualizado', user, oficina_cod)
    
    def alterar_margem(self, oficina_cod, user, id, margem_lucro):
        payload = {"margem_lucro": margem_lucro}
        self.repository.update(oficina_cod, id, payload)
        self.save_event_classname(id, Peca.__name__, payload, 'peca_margem_atualizado', user, oficina_cod)

    def alterar_prazo(self, oficina_cod, user, id, prazo_medio_entrega):
        payload = {"prazo_medio_entrega": prazo_medio_entrega}
        self.repository.update(oficina_cod, id, payload)
        self.save_event_classname(id, Peca.__name__, payload, 'peca_prazo_atualizado', user, oficina_cod)

    def alterar_custo(self, oficina_cod, user, id, custo):
        payload = {"custo": custo}
        self.repository.update(oficina_cod, id, payload)
        self.save_event_classname(id, Peca.__name__, payload, 'peca_custo_atualizado', user, oficina_cod)