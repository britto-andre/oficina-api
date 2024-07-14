from fastapi import Depends, APIRouter, HTTPException, Body, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from src.app.common.security.security_util import SecurityConfig, active_user

router = APIRouter()
service = SecurityConfig()

@router.post('/login')
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    try:
        token = service.getToken(form_data.username, form_data.password)
        return {'message': 'Token gerado', 'access_token': token, 'token_type': 'bearer'}
    except:
       raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST,
           detail={'message': 'Usuário ou senha inválidos'})

@router.get('/')
async def detail(user: Annotated[dict, Depends(active_user)]):
    return user