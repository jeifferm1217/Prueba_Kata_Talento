from pydantic import BaseModel, EmailStr

# Registrar usuario
class RegistrarUsuario(BaseModel):
    nombre_usuario: str
    correo: EmailStr
    contraseña: str

# Sesión (login)
class SesionUsuario(BaseModel):
    nombre_usuario: str
    contraseña: str

# Respuesta al registrar u obtener usuario
class UsuarioResponse(BaseModel):
    id_usuario: int
    nombre_usuario: str
    correo: str
    activo: bool

    class Config:
        from_attributes = True 

    