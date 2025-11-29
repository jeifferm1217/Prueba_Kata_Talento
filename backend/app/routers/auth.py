from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = auth_service.autenticar_usuario(
        db,
        nombre_usuario=form_data.username,
        password=form_data.password
    )

    if not usuario:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")

    token = auth_service.crear_token(usuario.nombre_usuario)

    return {"access_token": token, "token_type": "bearer"}
