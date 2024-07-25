from fastapi import Depends, FastAPI
from src.app.common.security_util import active_user_only, active_user
from src.app.controller.usuario_controller import router as UsuarioRouter
from src.app.controller.oficina_controller import router as OficinaRouter
from src.app.controller.event_controller import router as EventRouter
from src.app.controller.servico_controller import router as ServicoRouter
from src.app.controller.peca_controller import router as PecaRouter
from src.app.controller.cliente_controller import router as ClienteRouter
from src.app.controller.veiculo_controller import router as veiculoRouter
from src.app.controller.orcamento_controller import router as OrcamentoRouter

app = FastAPI(title="Oficina API")
PROTECTED_ONLY_USER = [Depends(active_user_only)]
PROTECTED = [Depends(active_user)]

app.include_router(UsuarioRouter, tags=['Usuário'], prefix='/usuario')
app.include_router(OficinaRouter, tags=['Oficina'], prefix='/oficina', dependencies=PROTECTED_ONLY_USER)
app.include_router(EventRouter, tags=['Events'], prefix='/events', dependencies=PROTECTED)
app.include_router(ServicoRouter, tags=['Serviços'], prefix='/servicos', dependencies=PROTECTED)
app.include_router(PecaRouter, tags=['Peças'], prefix='/pecas', dependencies=PROTECTED)
app.include_router(ClienteRouter, tags=['Clientes'], prefix='/clientes', dependencies=PROTECTED)
app.include_router(veiculoRouter, tags=['Veiculos'], prefix='/veiculos', dependencies=PROTECTED)
app.include_router(OrcamentoRouter, tags=['Orçamentos'], prefix='/orcamentos', dependencies=PROTECTED)

@app.get('/', tags=['Root'])
async def home():
    return {'API':'Oficina Service'}