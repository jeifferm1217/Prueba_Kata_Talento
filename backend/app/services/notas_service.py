from sqlalchemy.orm import Session
from models.models import Notas

# Crear nota
def crear_nota(db: Session, id_usuario: int, titulo: str, contenido_markdown: str):
    nueva_nota = Notas(
        id_usuario=id_usuario,
        titulo=titulo,
        contenido_markdown=contenido_markdown
    )
    db.add(nueva_nota)
    db.commit()
    db.refresh(nueva_nota)
    return nueva_nota

# Listar notas de un usuario
def listar_notas(db: Session, id_usuario: int):
    return db.query(Notas).filter(Notas.id_usuario == id_usuario).all()

# Obtener una nota por ID
def obtener_nota(db: Session, id_nota: int, id_usuario: int):
    return db.query(Notas).filter(
        Notas.id_nota == id_nota,
        Notas.id_usuario == id_usuario
    ).first()

# Actualizar una nota
def actualizar_nota(db: Session, id_nota: int, id_usuario: int, titulo: str, contenido_markdown: str):
    nota = obtener_nota(db, id_nota, id_usuario)
    if nota:
        nota.titulo = titulo
        nota.contenido_markdown = contenido_markdown
        db.commit()
        db.refresh(nota)
    return nota

# Eliminar una nota
def eliminar_nota(db: Session, id_nota: int, id_usuario: int):
    nota = obtener_nota(db, id_nota, id_usuario)
    if nota:
        db.delete(nota)
        db.commit()
    return nota
