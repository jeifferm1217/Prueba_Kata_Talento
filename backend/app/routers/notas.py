from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from services import notas_service
from utils.security import obtener_usuario_actual
from schemas.notas import NotaCrear,NotaActualizar, NotaRespuesta
from typing import List

router = APIRouter(
    prefix="/notas",
    tags=["Notas"]
)

# Crear nota
@router.post("/", response_model=NotaRespuesta, status_code=status.HTTP_201_CREATED)
def crear_nota(nota: NotaCrear, db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
    return notas_service.crear_nota(db, usuario.id_usuario, nota.titulo, nota.contenido_markdown)

# Listar notas
@router.get("/", response_model=List[NotaRespuesta])
def listar_notas(db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
    return notas_service.listar_notas(db, usuario.id_usuario)

# Obtener nota por ID
@router.get("/{id_nota}", response_model=NotaRespuesta)
def obtener_nota(id_nota: int, db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
    nota = notas_service.obtener_nota(db, id_nota, usuario.id_usuario)
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    return nota

# Actualizar nota
@router.put("/{id_nota}", response_model=NotaRespuesta)
def actualizar_nota(id_nota: int, nota: NotaActualizar, db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
    nota_actualizada = notas_service.actualizar_nota(db, id_nota, usuario.id_usuario, nota.titulo, nota.contenido_markdown)
    if not nota_actualizada:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    return nota_actualizada

# Eliminar nota
@router.delete("/{id_nota}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_nota(id_nota: int, db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
    nota_eliminada = notas_service.eliminar_nota(db, id_nota, usuario.id_usuario)
    if not nota_eliminada:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    return None
