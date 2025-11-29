from pydantic import BaseModel, Field

class CategoriaCrear(BaseModel):
    nombre: str = Field(..., example="Guitarras")

class CategoriaRespuesta(BaseModel):
    id_categoria: int
    nombre: str

    class Config:
        orm_mode = True
