from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.models import Usuario

# Configuración hashing
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# Configuración JWT
SECRET_KEY = "mi-clave-super-secreta-cambiar-en-produccion"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# --------------------------
# Funciones de hashing
# --------------------------
def hash_contraseña(password: str) -> str:
    print(">>> Tipo de password recibido:", type(password))  # Debug
    print(">>> Valor de password:", password)  # Debug
    return pwd_context.hash(password)


def verificar_contraseña(password_plana: str, password_hash: str):
    """
    Antes de verificar también cortamos a 72 por seguridad.
    """
    if len(password_plana) > 72:
        password_plana = password_plana[:72]

    return pwd_context.verify(password_plana, password_hash)

# --------------------------
# Funciones JWT
# --------------------------
def crear_token_acceso(data: dict, expires_delta: timedelta | None = None):
    """Crea un token JWT."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))

    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verificar_token(token: str):
    """Decodifica un JWT y extrae el usuario."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        return username
    except JWTError:
        return None


# --------------------------
# Usuario actual
# --------------------------
def obtener_usuario_actual(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):

    credenciales_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar el token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    username = verificar_token(token)
    if not username:
        raise credenciales_exception

    usuario = db.query(Usuario).filter(Usuario.nombre_usuario == username).first()
    if not usuario:
        raise credenciales_exception

    return usuario
