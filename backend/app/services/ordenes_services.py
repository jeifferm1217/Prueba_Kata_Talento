from sqlalchemy.orm import Session
from datetime import datetime
from app.models.models import Carrito, ItemCarrito, Orden, DetalleOrden

def crear_orden(db: Session, id_usuario: int):
    carrito = db.query(Carrito).filter(Carrito.id_usuario == id_usuario).first()

    if not carrito or len(carrito.items) == 0:
        raise Exception("El carrito está vacío")

    total = sum(item.cantidad * item.precio_unitario for item in carrito.items)

    nueva = Orden(
        id_usuario=id_usuario,
        total=total,
        fecha=datetime.now(),
        estado="PENDIENTE"
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    for item in carrito.items:
        detalle = DetalleOrden(
            id_orden=nueva.id_orden,
            id_producto=item.id_producto,
            cantidad=item.cantidad,
            precio_unitario=item.precio_unitario
        )
        db.add(detalle)

    carrito.items.clear()
    db.commit()

    return nueva

def listar_ordenes_usuario(db: Session, id_usuario: int):
    return db.query(Orden).filter(Orden.id_usuario == id_usuario).all()
