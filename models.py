# ============================================================
# MODELOS DO BANCO DE DADOS
# ============================================================

from sqlalchemy import Column, Integer, String, Boolean

from database import Base


# ============================================================
# TABELA DE TAREFAS
# ============================================================

class Task(Base):

    # Nome da tabela no banco

    __tablename__ = "tasks"


    # ========================================================
    # COLUNAS
    # ========================================================

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=True
    )

    completed = Column(
        Boolean,
        default=False
    )