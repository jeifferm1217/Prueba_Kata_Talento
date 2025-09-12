from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.usuarios import RegistrarUsuario, UsuarioResponse

from services import auth_service

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

# Crear usuario (registro)
@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario: RegistrarUsuario, db: Session = Depends(get_db)):
    db_usuario = auth_service.obtener_usuario_por_nombre(db, usuario.nombre_usuario)
    if db_usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El nombre de usuario ya está registrado"
        )
    return auth_service.crear_usuario(db, usuario.nombre_usuario, usuario.correo, usuario.contraseña)

# Obtener usuario por nombre
@router.get("/{nombre_usuario}", response_model=UsuarioResponse)
def obtener_usuario(nombre_usuario: str, db: Session = Depends(get_db)):
    usuario = auth_service.obtener_usuario_por_nombre(db, nombre_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario
