# tests/conftest.py

import sys
from pathlib import Path


# Pega a pasta principal do projeto.
PROJECT_ROOT = Path(__file__).parent.parent


# Adiciona a pasta principal ao caminho de importação do Python.
sys.path.insert(0, str(PROJECT_ROOT))