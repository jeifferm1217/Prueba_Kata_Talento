from sqlalchemy import Column, Integer, Text, String, ForeignKey, DateTime, Boolean, Float
from datetime import datetime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func
from app.db.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre_usuario = Column(String(50), unique=True, nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    es_admin = Column(Boolean, default=False)

    carrito = relationship("Carrito", back_populates="usuario", uselist=False)
    ordenes = relationship("Orden", back_populates="usuario")

class Categoria(Base):
    __tablename__ = "categorias"

    id_categoria = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, nullable=False)

    productos = relationship("Producto", back_populates="categoria")


class Producto(Base):
    __tablename__ = "productos"

    id_producto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255))
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    imagen_url = Column(String(255))

    id_categoria = Column(Integer, ForeignKey("categorias.id_categoria"))
    categoria = relationship("Categoria", back_populates="productos")

    items_carrito = relationship("ItemCarrito", back_populates="producto")
    detalles_orden = relationship("DetalleOrden", back_populates="producto")

class Carrito(Base):
    __tablename__ = "carritos"

    id_carrito = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))

    usuario = relationship("Usuario", back_populates="carrito")
    items = relationship("ItemCarrito", back_populates="carrito", cascade="all, delete-orphan")


class ItemCarrito(Base):
    __tablename__ = "items_carrito"

    id_item = Column(Integer, primary_key=True, index=True)
    id_carrito = Column(Integer, ForeignKey("carritos.id_carrito"))
    id_producto = Column(Integer, ForeignKey("productos.id_producto"))
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)

    carrito = relationship("Carrito", back_populates="items")
    producto = relationship("Producto", back_populates="items_carrito")

class Orden(Base):
    __tablename__ = "ordenes"

    id_orden = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    total = Column(Float, nullable=False)
    fecha = Column(DateTime, default=datetime.now)
    estado = Column(String(20), default="PENDIENTE")

    usuario = relationship("Usuario", back_populates="ordenes")
    detalles = relationship("DetalleOrden", back_populates="orden", cascade="all, delete-orphan")


class DetalleOrden(Base):
    __tablename__ = "detalles_orden"

    id_detalle = Column(Integer, primary_key=True, index=True)
    id_orden = Column(Integer, ForeignKey("ordenes.id_orden"))
    id_producto = Column(Integer, ForeignKey("productos.id_producto"))
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)

    orden = relationship("Orden", back_populates="detalles")
    producto = relationship("Producto", back_populates="detalles_orden")