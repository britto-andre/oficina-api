from fastapi import FastAPI

app = FastAPI()

@app.get('/', tags=['Root'])
async def home():
    return {'API':'Oficina Service'}