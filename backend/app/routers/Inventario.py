from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services import inventarios_service
from app.utils.security import obtener_usuario_actual
from app.schemas.Inventario import InventarioActualizar

router = APIRouter(
    prefix="/inventario",
    tags=["Inventario (Admin)"]
)

@router.put("/{id_producto}")
def actualizar_stock(id_producto: int, data: InventarioActualizar, usuario=Depends(obtener_usuario_actual), db: Session = Depends(get_db)):
    if not usuario.es_admin:
        raise HTTPException(status_code=403, detail="Solo administradores pueden modificar el inventario")
    return inventarios_service.actualizar_stock(db, id_producto, data.stock)
