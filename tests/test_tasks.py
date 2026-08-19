# ============================================================
# TESTES DA TASK API
# ============================================================

# Importamos o TestClient.
#
# Ele permite fazer requisições HTTP para nossa API
# durante os testes.

from fastapi.testclient import TestClient


# Importamos nossa aplicação FastAPI.

from main import app


# ============================================================
# CLIENTE DE TESTES
# ============================================================

# Criamos um cliente que vai "conversar" com nossa API.

client = TestClient(app)


# ============================================================
# TESTE 1 — ROTA PRINCIPAL
# ============================================================

def test_home():

    # Fazemos uma requisição GET para "/".

    response = client.get("/")


    # Verificamos se a API respondeu HTTP 200.

    assert response.status_code == 200


    # Verificamos o conteúdo da resposta.

    assert response.json() == {
        "message": "Task API funcionando!"
    }


# ============================================================
# TESTE 2 — CRIAR TAREFA
# ============================================================

def test_create_task():

    # Dados que vamos enviar para nossa API.

    task = {
        "title": "Estudar Pytest",
        "description": "Aprender testes automatizados"
    }


    # Fazemos uma requisição POST.

    response = client.post(
        "/tasks",
        json=task
    )


    # A criação deve retornar HTTP 201.

    assert response.status_code == 201


    # Pegamos os dados retornados pela API.

    data = response.json()


    # Verificamos se o título foi salvo corretamente.

    assert data["title"] == "Estudar Pytest"


    # Verificamos a descrição.

    assert data["description"] == "Aprender testes automatizados"


    # Uma tarefa nova deve começar como não concluída.

    assert data["completed"] is False


# ============================================================
# TESTE 3 — BUSCAR TAREFA
# ============================================================

def test_get_task():

    # Primeiro criamos uma tarefa.

    task = {
        "title": "Testar busca",
        "description": "Testando GET"
    }


    create_response = client.post(
        "/tasks",
        json=task
    )


    # Pegamos o ID da tarefa criada.

    task_id = create_response.json()["id"]


    # Agora buscamos essa tarefa.

    response = client.get(
        f"/tasks/{task_id}"
    )


    # Esperamos HTTP 200.

    assert response.status_code == 200


    # Pegamos os dados retornados.

    data = response.json()


    # Conferimos o ID.

    assert data["id"] == task_id


    # Conferimos o título.

    assert data["title"] == "Testar busca"


# ============================================================
# TESTE 4 — TAREFA NÃO ENCONTRADA
# ============================================================

def test_get_task_not_found():

    # Tentamos buscar uma tarefa que não existe.

    response = client.get(
        "/tasks/999999"
    )


    # A API deve retornar HTTP 404.

    assert response.status_code == 404


    # Verificamos a mensagem de erro.

    assert response.json()["detail"] == "Tarefa não encontrada"