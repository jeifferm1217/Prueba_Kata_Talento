from pydantic import BaseModel, Field
from typing import List

# ----- Item dentro del carrito -----
class ItemCarrito(BaseModel):
    id_item: int
    id_producto: int
    nombre_producto: str
    cantidad: int
    subtotal: float

    class Config:
        orm_mode = True

# ----- Agregar item -----
class ItemAgregar(BaseModel):
    id_producto: int = Field(..., example=3)
    cantidad: int = Field(..., ge=1, example=2)

# ----- Carrito completo -----
class CarritoRespuesta(BaseModel):
    id_carrito: int
    items: List[ItemCarrito]
    total: float

    class Config:
        orm_mode = True
