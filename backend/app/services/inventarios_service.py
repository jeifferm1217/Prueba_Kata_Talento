from sqlalchemy.orm import Session
from app.models.models import Producto

def actualizar_stock(db: Session, id_producto: int, stock: int):
    producto = db.query(Producto).filter(Producto.id_producto == id_producto).first()
    if not producto:
        return None

    producto.stock = stock
    db.commit()
    db.refresh(producto)
    return producto
