from pydantic import BaseModel
from typing import List

class DetalleOrdenRespuesta(BaseModel):
    id_detalle: int
    id_producto: int
    nombre_producto: str
    cantidad: int
    precio_unitario: float
    subtotal: float

    class Config:
        orm_mode = True

class OrdenRespuesta(BaseModel):
    id_orden: int
    id_usuario: int
    total: float
    fecha: str
    estado: str
    detalles: List[DetalleOrdenRespuesta]

    class Config:
        orm_mode = True
