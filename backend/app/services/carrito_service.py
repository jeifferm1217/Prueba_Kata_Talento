from sqlalchemy.orm import Session
from app.models.models import Carrito, ItemCarrito, Producto

def obtener_carrito_usuario(db: Session, id_usuario: int):
    carrito = db.query(Carrito).filter(Carrito.id_usuario == id_usuario).first()

    if not carrito:
        carrito = Carrito(id_usuario=id_usuario)
        db.add(carrito)
        db.commit()
        db.refresh(carrito)

    return carrito

def agregar_item(db: Session, id_usuario: int, id_producto: int, cantidad: int):
    carrito = obtener_carrito_usuario(db, id_usuario)
    producto = db.query(Producto).filter(Producto.id_producto == id_producto).first()

    if not producto:
        raise Exception("Producto no encontrado")

    item = db.query(ItemCarrito).filter(
        ItemCarrito.id_carrito == carrito.id_carrito,
        ItemCarrito.id_producto == id_producto
    ).first()

    if item:
        item.cantidad += cantidad
    else:
        item = ItemCarrito(
            id_carrito=carrito.id_carrito,
            id_producto=id_producto,
            cantidad=cantidad,
            precio_unitario=producto.precio
        )
        db.add(item)

    db.commit()
    db.refresh(carrito)
    return carrito

def eliminar_item(db: Session, id_usuario: int, id_item: int):
    carrito = obtener_carrito_usuario(db, id_usuario)

    item = db.query(ItemCarrito).filter(
        ItemCarrito.id_carrito == carrito.id_carrito,
        ItemCarrito.id_item == id_item
    ).first()

    if not item:
        return False

    db.delete(item)
    db.commit()
    return True
