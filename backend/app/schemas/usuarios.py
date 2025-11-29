from pydantic import BaseModel, EmailStr

class UsuarioCrear(BaseModel):
    nombre_usuario: str
    correo: EmailStr
    password: str

class UsuarioRespuesta(BaseModel):
    id_usuario: int
    nombre_usuario: str
    correo: EmailStr

    class Config:
        from_attributes = True
