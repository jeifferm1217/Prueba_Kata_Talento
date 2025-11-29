from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.models import Usuario

# ----------------------------------------------------
# Configuración de seguridad
# ----------------------------------------------------
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


# Configuración del JWT
SECRET_KEY = "SUPER_SECRETO_CAMBIALO"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


# -------------------------------
# HASHING
# -------------------------------
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verificar_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# -------------------------------
# CREAR USUARIO
# -------------------------------
def crear_usuario(db: Session, nombre_usuario: str, correo: str, password: str):
    usuario = Usuario(
        nombre_usuario=nombre_usuario,
        correo=correo,
        password=hash_password(password)
    )

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario


# -------------------------------
# OBTENER USUARIO
# -------------------------------
def obtener_usuario_por_nombre(db: Session, nombre_usuario: str):
    return db.query(Usuario).filter(Usuario.nombre_usuario == nombre_usuario).first()


# -------------------------------
# AUTENTICAR USUARIO (login)
# -------------------------------
def autenticar_usuario(db: Session, nombre_usuario: str, password: str):
    usuario = obtener_usuario_por_nombre(db, nombre_usuario)

    if not usuario:
        return None

    if not verificar_password(password, usuario.password):
        return None

    return usuario


# -------------------------------
# CREAR TOKEN JWT
# -------------------------------
def crear_token(nombre_usuario: str):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {
        "sub": nombre_usuario,
        "exp": expire
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token