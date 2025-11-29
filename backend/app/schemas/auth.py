from pydantic import BaseModel

class LoginRequest(BaseModel):
    nombre_usuario: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
