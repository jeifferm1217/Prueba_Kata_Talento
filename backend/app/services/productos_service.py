from sqlalchemy.orm import Session
from app.models.models import Producto
from app.schemas.Producto import ProductoCrear, ProductoActualizar

def crear_producto(db: Session, data: ProductoCrear):
    nuevo = Producto(
        nombre=data.nombre,
        descripcion=data.descripcion,
        precio=data.precio,
        stock=data.stock,
        id_categoria=data.id_categoria,
        imagen_url=data.imagen_url
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def listar_productos(db: Session):
    return db.query(Producto).all()

def productos_por_categoria(db: Session, id_categoria: int):
    return db.query(Producto).filter(Producto.id_categoria == id_categoria).all()

def buscar_productos(db: Session, query: str):
    return db.query(Producto).filter(
        Producto.nombre.ilike(f"%{query}%")
    ).all()

def obtener_producto(db: Session, id_producto: int):
    return db.query(Producto).filter(Producto.id_producto == id_producto).first()

def actualizar_producto(db: Session, id_producto: int, data: ProductoActualizar):
    producto = obtener_producto(db, id_producto)
    if not producto:
        return None

    for campo, valor in data.dict(exclude_unset=True).items():
        setattr(producto, campo, valor)

    db.commit()
    db.refresh(producto)
    return producto

def eliminar_producto(db: Session, id_producto: int):
    producto = obtener_producto(db, id_producto)
    if not producto:
        return False

    db.delete(producto)
    db.commit()
    return True
