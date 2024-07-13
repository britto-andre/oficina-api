from fastapi import FastAPI

from src.app.controller.servico_controller import router as ServicoRouter

app = FastAPI()

app.include_router(ServicoRouter, tags=['Serviço'], prefix='/servico')

@app.get('/', tags=['Root'])
async def home():
    return {'API':'Oficina Service'}