from sqlalchemy.orm import Session
from models.models import Usuarios
from utils import security

# Crear usuario
def crear_usuario(db: Session, nombre_usuario: str, correo: str, contraseña: str):
    contraseña_hash = security.hash_contraseña(contraseña)
    db_usuario = Usuarios(
        nombre_usuario=nombre_usuario,
        correo=correo,
        contraseña_hash=contraseña_hash
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

# Obtener usuario por nombre
def obtener_usuario_por_nombre(db: Session, nombre_usuario: str):
    return db.query(Usuarios).filter(Usuarios.nombre_usuario == nombre_usuario).first()

# Autenticar usuario
def autenticar_usuario(db: Session, nombre_usuario: str, contraseña: str):
    usuario = obtener_usuario_por_nombre(db, nombre_usuario)
    if not usuario or not security.verificar_contraseña(contraseña, usuario.contraseña_hash):
        return None
    return usuario

# Crear token de acceso
def crear_token_acceso(nombre_usuario: str) -> str:
    data = {"sub": nombre_usuario}
    return security.crear_token_acceso(data)
