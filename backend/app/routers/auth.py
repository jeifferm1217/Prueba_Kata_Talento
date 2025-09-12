from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from db.database import get_db
from services import auth_service
from schemas.token import Token

router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"]
)

# Login → devuelve JWT
@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = auth_service.autenticar_usuario(db, form_data.username, form_data.password)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = auth_service.crear_token_acceso(usuario.nombre_usuario)
    return {"access_token": token, "token_type": "bearer"}
