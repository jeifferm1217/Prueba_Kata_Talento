from pydantic import BaseModel
from typing import Optional


class NotaCrear(BaseModel):
    titulo: str
    contenido_markdown: str


class NotaActualizar(BaseModel):
    titulo: Optional[str] = None
    contenido_markdown: Optional[str] = None


class NotaRespuesta(BaseModel):
    id_nota: int
    titulo: str
    contenido_markdown: str
    id_usuario: int

    class Config:
        from_attributes = True  
