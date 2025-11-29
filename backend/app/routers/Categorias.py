from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.Categorias import CategoriaCrear, CategoriaRespuesta
from app.services import categorias_service

router = APIRouter(
    prefix="/categorias",
    tags=["Categorías - Tienda Musical"]
)

@router.post("/", response_model=CategoriaRespuesta)
def crear_categoria(cat: CategoriaCrear, db: Session = Depends(get_db)):
    return categorias_service.crear_categoria(db, cat)

@router.get("/", response_model=list[CategoriaRespuesta])
def listar_categorias(db: Session = Depends(get_db)):
    return categorias_service.listar_categorias(db)
