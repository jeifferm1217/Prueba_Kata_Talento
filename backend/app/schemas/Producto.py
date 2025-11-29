from pydantic import BaseModel, Field
from typing import Optional

# ----------- Crear producto -----------
class ProductoCrear(BaseModel):
    nombre: str = Field(..., min_length=3, example="Guitarra Acústica Fender CD-60")
    descripcion: str = Field(..., example="Guitarra acústica de 6 cuerdas ideal para principiantes.")
    precio: float = Field(..., ge=0, example=550000)
    stock: int = Field(..., ge=0, example=10)
    id_categoria: int = Field(..., example=1)
    imagen_url: Optional[str] = Field(None, example="https://cdn.tienda.com/img/guitarra.jpg")

# ----------- Actualizar producto -----------
class ProductoActualizar(BaseModel):
    nombre: Optional[str]
    descripcion: Optional[str]
    precio: Optional[float]
    stock: Optional[int]
    id_categoria: Optional[int]
    imagen_url: Optional[str]

# ----------- Respuesta producto -----------
class ProductoRespuesta(BaseModel):
    id_producto: int
    nombre: str
    descripcion: str
    precio: float
    stock: int
    id_categoria: int
    imagen_url: Optional[str]

    class Config:
        orm_mode = True
