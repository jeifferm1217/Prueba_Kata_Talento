from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.utils.security import obtener_usuario_actual
from app.schemas.Producto import ProductoCrear, ProductoActualizar, ProductoRespuesta
from app.services import productos_service

router = APIRouter(
    prefix="/productos",
    tags=["Productos - Tienda Musical"]
)

# Crear producto
@router.post("/productos")
def crear_producto(producto: ProductoCrear, 
                   db: Session = Depends(get_db),
                   usuario_actual = Depends(obtener_usuario_actual)):
    return productos_service.crear_producto(db, producto, usuario_actual)
# Listar productos
@router.get("/", response_model=List[ProductoRespuesta])
def listar_productos(db: Session = Depends(get_db)):
    return productos_service.listar_productos(db)

# Buscar productos por categoría
@router.get("/categoria/{id_categoria}", response_model=List[ProductoRespuesta])
def productos_por_categoria(id_categoria: int, db: Session = Depends(get_db)):
    return productos_service.productos_por_categoria(db, id_categoria)

# Buscar productos por nombre
@router.get("/buscar", response_model=List[ProductoRespuesta])
def buscar_productos(q: str, db: Session = Depends(get_db)):
    return productos_service.buscar_productos(db, q)

# Obtener producto por ID
@router.get("/{id_producto}", response_model=ProductoRespuesta)
def obtener_producto(id_producto: int, db: Session = Depends(get_db)):
    producto = productos_service.obtener_producto(db, id_producto)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

# Actualizar producto
@router.put("/{id_producto}", response_model=ProductoRespuesta)
def actualizar_producto(id_producto: int, datos: ProductoActualizar, db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
    if not usuario.es_admin:
        raise HTTPException(status_code=403, detail="No tienes permisos para actualizar productos")
    actualizado = productos_service.actualizar_producto(db, id_producto, datos)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return actualizado

# Eliminar producto
@router.delete("/{id_producto}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_producto(id_producto: int, db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
    if not usuario.es_admin:
        raise HTTPException(status_code=403, detail="No tienes permisos para eliminar productos")
    eliminado = productos_service.eliminar_producto(db, id_producto)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return None
