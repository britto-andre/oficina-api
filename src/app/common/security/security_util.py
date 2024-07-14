import pyrebase
import firebase_admin
from firebase_admin import credentials, auth
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from typing import Annotated

from src.app.common.utils.logger import logger
from src.app.common.common_settings import CommonSettings

security = HTTPBearer()

async def token_required(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        user = auth.verify_id_token(token)
        return user
    except Exception as e:
        logger.warn(f'Auth Erro {e}')
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não logado ou sessão inválida.",
            headers={"WWW-Authenticate": "Bearer"},
        )

async def active_user(user: Annotated[dict, Depends(token_required)]):
    return user

class SecurityConfig:

    def __init__(self):
        self.settings = CommonSettings()
        self.firebase = pyrebase.initialize_app({
            "apiKey": self.settings.firebase_apiKey,
            "authDomain": self.settings.firebase_authDomain,
            "databaseURL": self.settings.firebase_databaseURL,
            "storageBucket": self.settings.firebase_storageBucket,
        })
        firebase_admin.initialize_app(credentials.Certificate(self.settings.FIREBASE_CONFIG))
        logger.info(f'Firebase App {firebase_admin.get_app().project_id} iniciado.')
        logger.info(f'Create SecurityConfig with Domain {self.settings.firebase_authDomain}')
        
    def getToken(self, email, password):
         user = self.firebase.auth().sign_in_with_email_and_password(email, password)
         logger.info(f'User getToken {user['email']}')
         return user['idToken']