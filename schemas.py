# ============================================================
# SCHEMAS DA API
# ============================================================

from pydantic import BaseModel
from typing import Optional


# ============================================================
# CRIAÇÃO
# ============================================================

class TaskCreate(BaseModel):

    title: str

    description: Optional[str] = None


# ============================================================
# ATUALIZAÇÃO
# ============================================================

class TaskUpdate(BaseModel):

    title: Optional[str] = None

    description: Optional[str] = None

    completed: Optional[bool] = None


# ============================================================
# RESPOSTA
# ============================================================

class TaskResponse(BaseModel):

    id: int

    title: str

    description: Optional[str]

    completed: bool

    class Config:
        from_attributes = True