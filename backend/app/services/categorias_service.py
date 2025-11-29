from sqlalchemy.orm import Session
from app.models.models import Categoria
from app.schemas.Categorias import CategoriaCrear

def crear_categoria(db: Session, cat: CategoriaCrear):
    nueva = Categoria(nombre=cat.nombre)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def listar_categorias(db: Session):
    return db.query(Categoria).all()
