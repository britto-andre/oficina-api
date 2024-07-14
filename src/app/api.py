from fastapi import Depends, FastAPI
from src.app.common.security.security_util import token_required
from src.app.controller.usuario_controller import router as UsuarioRouter
from src.app.controller.servico_controller import router as ServicoRouter

app = FastAPI(title="Oficina API")
PROTECTED = [Depends(token_required)]

app.include_router(ServicoRouter, tags=['Serviço'], prefix='/servico', dependencies=PROTECTED)
app.include_router(UsuarioRouter, tags=['Usuário'], prefix='/usuario')

@app.get('/', tags=['Root'])
async def home():
    return {'API':'Oficina Service'}