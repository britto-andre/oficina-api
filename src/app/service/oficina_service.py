from src.app.common.default_service import DefaultService
from src.app.entity.oficina import Oficina
from src.app.repository.oficina_repository import OficinaRepository
from src.app.common.str_util import replace_last, normalize

class OficinaService(DefaultService):

    def __init__(self) -> None:
        super().__init__()
        self.repository = OficinaRepository()

    def _build_codigo(self, nome):
        codigo = ''.join(c for c in nome if c.isalnum())[:10]
        codigo = normalize(codigo.ljust(10, '0')).lower()
        return self._check_codigo(codigo, 0)

    def _check_codigo(self, codigo, index:int):
        oficina = self.repository.find_one_by_codigo(codigo)
        if not oficina:
            return codigo
        else:
            index += 1
            codigo = replace_last(codigo, str(index))
            return self._check_codigo(codigo, index)

    def create(self, obj: Oficina, user):
        oficina = self.repository.find_one_by_email(obj.email)
        if not oficina:
            obj.codigo = self._build_codigo(obj.nome)
            obj_id = self.repository.create(obj)
            self.save_event(obj_id, obj, 'oficina_criada', user, obj.codigo)
            return obj_id
        else:
            return None
    
    def find_one_by_email(self, email):
        return self.repository.find_one_by_email(email)