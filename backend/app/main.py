from fastapi import FastAPI
from db.database import Base, engine
from routers import auth, usuarios, notas

# Crear las tablas en la base de datos (si no existen)
Base.metadata.create_all(bind=engine)

# Instancia de FastAPI
app = FastAPI(
    title="Notas con Markdown",
    version="1.0.0"
)

# Incluir routers
app.include_router(auth.router)
app.include_router(usuarios.router)
app.include_router(notas.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)