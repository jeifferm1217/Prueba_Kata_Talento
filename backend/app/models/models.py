from sqlalchemy import Column, Integer, Text, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func
from db.database import Base

class Usuarios(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre_usuario = Column(String, unique=True, index=True, nullable=False)
    correo = Column(String, unique=True, index=True, nullable=False)
    contraseña_hash = Column(String, nullable=False)
    activo = Column(Boolean, default=True)

    notas = relationship("Notas", back_populates="usuario", cascade="all, delete-orphan")

class Notas(Base):
    __tablename__ = "notas"

    id_nota = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario", ondelete="CASCADE"), nullable=False)
    titulo = Column(String(150), nullable=False)
    contenido_markdown = Column(Text, nullable=False)

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now())
    
    usuario = relationship("Usuarios", back_populates="notas")
