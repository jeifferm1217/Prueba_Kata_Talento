from fastapi import FastAPI
from app.routers import Ordenes
from app.routers import Categorias, Carrito_De_Compras, Inventario, Productos
from app.db.database import engine, Base
from app.routers import auth, usuarios

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="tienda_musical_api",
    version="1.0.0"
)

# Routers
app.include_router(usuarios.router)  # <-- SIN PREFIX AQUÍ
app.include_router(auth.router)
app.include_router(Categorias.router)
app.include_router(Productos.router)
app.include_router(Inventario.router)
app.include_router(Carrito_De_Compras.router)
app.include_router(Ordenes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
