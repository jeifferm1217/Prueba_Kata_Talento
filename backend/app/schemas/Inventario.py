from pydantic import BaseModel, Field

class InventarioActualizar(BaseModel):
    stock: int = Field(..., ge=0, example=25)
