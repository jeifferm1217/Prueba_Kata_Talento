from sqlalchemy.orm import Session
from app.utils.security import hash_contraseña

from app.models.models import Usuario
from app.schemas.usuarios import UsuarioCrear   # ← Ruta corregida


def crear_usuario(db: Session, data: UsuarioCrear):
    usuario = Usuario(
        nombre_usuario=data.nombre_usuario,
        correo=data.correo,
        password=hash_contraseña(data.password),  # ← Campo ya corregido
        es_admin=False
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario


def obtener_por_id(db: Session, id_usuario: int):
    return db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()


def obtener_por_username(db: Session, username: str):
    return db.query(Usuario).filter(Usuario.nombre_usuario == username).first()
