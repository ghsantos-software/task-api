# ============================================================
# API DE GERENCIAMENTO DE TAREFAS
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from database import engine, SessionLocal, Base
from models import Task
from schemas import TaskCreate, TaskUpdate, TaskResponse


# ============================================================
# 1. CRIANDO AS TABELAS
# ============================================================

# Essa linha verifica os modelos existentes e cria
# as tabelas que ainda não existem.

Base.metadata.create_all(bind=engine)


# ============================================================
# 2. CRIANDO A APLICAÇÃO
# ============================================================

app = FastAPI(
    title="Task API",
    description="API de gerenciamento de tarefas",
    version="2.0.0"
)


# ============================================================
# 3. CRIANDO UMA SESSÃO DO BANCO
# ============================================================

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


# ============================================================
# 4. ROTA PRINCIPAL
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Task API funcionando!"
    }


# ============================================================
# 5. LISTAR TAREFAS
# ============================================================

@app.get(
    "/tasks",
    response_model=list[TaskResponse]
)
def get_tasks(
    db: Session = Depends(get_db)
):

    # Busca todas as tarefas no banco.

    tasks = db.query(Task).all()

    return tasks


# ============================================================
# 6. BUSCAR UMA TAREFA
# ============================================================

@app.get(
    "/tasks/{task_id}",
    response_model=TaskResponse
)
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):

    # Procura a tarefa pelo ID.

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()


    # Se não encontrou:

    if task is None:

        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )


    return task


# ============================================================
# 7. CRIAR TAREFA
# ============================================================

@app.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=201
)
def create_task(
    task_data: TaskCreate,
    db: Session = Depends(get_db)
):

    # Criamos um objeto Task.

    new_task = Task(

        title=task_data.title,

        description=task_data.description,

        completed=False
    )


    # Adicionamos o objeto à sessão.

    db.add(new_task)


    # Salvamos no banco.

    db.commit()


    # Atualizamos o objeto para receber o ID
    # gerado pelo banco.

    db.refresh(new_task)


    return new_task


# ============================================================
# 8. ATUALIZAR TAREFA
# ============================================================

@app.put(
    "/tasks/{task_id}",
    response_model=TaskResponse
)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db)
):

    # Procuramos a tarefa.

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()


    if task is None:

        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )


    # Atualizamos somente os campos enviados.

    if task_data.title is not None:

        task.title = task_data.title


    if task_data.description is not None:

        task.description = task_data.description


    if task_data.completed is not None:

        task.completed = task_data.completed


    # Salvamos as alterações.

    db.commit()

    db.refresh(task)


    return task


# ============================================================
# 9. DELETAR TAREFA
# ============================================================

@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):

    # Procuramos a tarefa.

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()


    if task is None:

        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )


    # Removemos a tarefa.

    db.delete(task)


    # Salvamos a alteração.

    db.commit()


    return {
        "message": "Tarefa deletada com sucesso"
    }