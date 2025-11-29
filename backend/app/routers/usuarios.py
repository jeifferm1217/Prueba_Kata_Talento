from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.usuarios import UsuarioCrear, UsuarioRespuesta
from app.services import auth_service

router = APIRouter()

@router.post("/", response_model=UsuarioRespuesta, status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario: UsuarioCrear, db: Session = Depends(get_db)):

    return auth_service.crear_usuario(
        db=db,
        nombre_usuario=usuario.nombre_usuario,
        correo=usuario.correo,
        password=usuario.password
    )


@router.get("/{nombre_usuario}", response_model=UsuarioRespuesta)
def obtener_usuario(nombre_usuario: str, db: Session = Depends(get_db)):

    usuario = auth_service.obtener_usuario_por_nombre(db, nombre_usuario)
    
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return usuario
