from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services import carrito_service
from app.utils.security import obtener_usuario_actual
from app.schemas.Carrito import CarritoRespuesta, ItemAgregar

router = APIRouter(
    prefix="/carrito",
    tags=["Carrito de Compras"]
)

# Ver mi carrito
@router.get("/", response_model=CarritoRespuesta)
def ver_carrito(usuario=Depends(obtener_usuario_actual), db: Session = Depends(get_db)):
    return carrito_service.obtener_carrito_usuario(db, usuario.id_usuario)

# Agregar producto al carrito
@router.post("/agregar", response_model=CarritoRespuesta)
def agregar_item(item: ItemAgregar, usuario=Depends(obtener_usuario_actual), db: Session = Depends(get_db)):
    return carrito_service.agregar_item(db, usuario.id_usuario, item.id_producto, item.cantidad)

# Eliminar ítem del carrito
@router.delete("/eliminar/{id_item}")
def eliminar_item(id_item: int, usuario=Depends(obtener_usuario_actual), db: Session = Depends(get_db)):
    return carrito_service.eliminar_item(db, usuario.id_usuario, id_item)
