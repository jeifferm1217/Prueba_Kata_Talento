from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services import ordenes_services
from app.utils.security import obtener_usuario_actual
from app.schemas.Ordenes import OrdenRespuesta

router = APIRouter(
    prefix="/ordenes",
    tags=["Órdenes - Tienda Musical"]
)

# Crear una orden desde el carrito
@router.post("/crear", response_model=OrdenRespuesta)
def crear_orden(usuario=Depends(obtener_usuario_actual), db: Session = Depends(get_db)):
    return ordenes_services.crear_orden(db, usuario.id_usuario)

# Ver mis órdenes
@router.get("/", response_model=list[OrdenRespuesta])
def listar_ordenes(usuario=Depends(obtener_usuario_actual), db: Session = Depends(get_db)):
    return ordenes_services.listar_ordenes_usuario(db, usuario.id_usuario)
