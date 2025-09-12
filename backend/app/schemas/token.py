from pydantic import BaseModel
from typing import Optional


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class DatosToken(BaseModel):
    nombre_usuario: str | None = None