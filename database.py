# ============================================================
# CONEXÃO COM O BANCO DE DADOS
# ============================================================

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# ============================================================
# CONFIGURAÇÕES DO BANCO
# ============================================================

# Pegamos as informações através de variáveis de ambiente.
#
# Isso é importante porque não queremos colocar senhas
# diretamente no código.

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/tasks"
)


# ============================================================
# CRIANDO A CONEXÃO
# ============================================================

engine = create_engine(
    DATABASE_URL
)


# ============================================================
# CRIANDO A SESSÃO
# ============================================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# ============================================================
# BASE DOS MODELOS
# ============================================================

Base = declarative_base()