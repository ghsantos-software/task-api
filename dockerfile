# ============================================================
# 1. IMAGEM BASE
# ============================================================

# Utilizamos uma imagem oficial do Python.
#
# slim é uma versão menor da imagem, contendo apenas
# o necessário para executar Python.

FROM python:3.12-slim


# ============================================================
# 2. DIRETÓRIO DE TRABALHO
# ============================================================

# Dentro do container, nossa aplicação ficará em /app.

WORKDIR /app


# ============================================================
# 3. COPIAR DEPENDÊNCIAS
# ============================================================

# Primeiro copiamos apenas o requirements.txt.
#
# Isso ajuda o Docker a aproveitar o cache das camadas.
# Se o código mudar, mas as dependências continuarem iguais,
# o Docker não precisa instalar tudo novamente.

COPY requirements.txt .


# ============================================================
# 4. INSTALAR DEPENDÊNCIAS
# ============================================================

RUN pip install --no-cache-dir -r requirements.txt


# ============================================================
# 5. COPIAR O CÓDIGO
# ============================================================

# Agora copiamos os arquivos da aplicação
# para dentro do container.

COPY . .


# ============================================================
# 6. EXPOR A PORTA
# ============================================================

# Nossa aplicação FastAPI utilizará a porta 8000.

EXPOSE 8000


# ============================================================
# 7. COMANDO PARA INICIAR A API
# ============================================================

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]