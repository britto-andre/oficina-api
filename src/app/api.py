from fastapi import Depends, FastAPI
from src.app.common.security_util import token_required
from src.app.controller.usuario_controller import router as UsuarioRouter
from src.app.controller.oficina_controller import router as OficinaRouter
from src.app.controller.servico_controller import router as ServicoRouter

app = FastAPI(title="Oficina API")
PROTECTED = [Depends(token_required)]

app.include_router(UsuarioRouter, tags=['Usuário'], prefix='/usuario')
app.include_router(OficinaRouter, tags=['Oficina'], prefix='/oficina', dependencies=PROTECTED)
app.include_router(ServicoRouter, tags=['Serviços'], prefix='/servicos', dependencies=PROTECTED)

@app.get('/', tags=['Root'])
async def home():
    return {'API':'Oficina Service'}