# Task API — Projeto DevOps

API REST de gerenciamento de tarefas desenvolvida em **Python com FastAPI**, construída como um projeto prático de aprendizado de **desenvolvimento, testes, containers, CI/CD e Cloud**.

O projeto está sendo desenvolvido de forma incremental: cada etapa adiciona uma tecnologia ou prática utilizada no mercado, permitindo acompanhar a evolução de uma aplicação local até uma infraestrutura completa em Cloud.

---

## 📌 Status do Projeto

🟢 **Em desenvolvimento**

### Já implementado

* [x] API REST com FastAPI
* [x] CRUD de tarefas
* [x] Validação de dados com Pydantic
* [x] SQLAlchemy
* [x] PostgreSQL
* [x] Testes automatizados com Pytest
* [x] Dockerfile
* [x] Docker Image
* [x] Docker Container
* [x] Docker Compose
* [x] Docker Network
* [x] Docker Volume
* [x] Variáveis de ambiente
* [x] `.gitignore`
* [x] Git
* [x] GitHub
* [x] README e documentação inicial

### Próximas etapas

* [ ] GitHub Actions — CI
* [ ] Executar testes automaticamente no GitHub
* [ ] Docker Build dentro da pipeline
* [ ] Dependabot
* [ ] Melhorias de segurança
* [ ] GitHub Secrets
* [ ] Amazon ECR
* [ ] AWS IAM
* [ ] AWS EC2
* [ ] Deploy da aplicação na EC2
* [ ] Pipeline CI/CD completa
* [ ] Infrastructure as Code com Terraform
* [ ] Kubernetes
* [ ] Amazon EKS
* [ ] Observabilidade
* [ ] Logs e métricas
* [ ] Prometheus
* [ ] Grafana

---

# 🧠 Sobre o Projeto

O objetivo deste projeto é construir uma aplicação simples e utilizá-la como laboratório para aprender conceitos de **DevOps na prática**.

A aplicação escolhida é uma API de gerenciamento de tarefas porque possui uma lógica simples, permitindo concentrar o aprendizado na infraestrutura e no ciclo de desenvolvimento.

A evolução planejada é:

```text
Python
   ↓
FastAPI
   ↓
PostgreSQL
   ↓
Pytest
   ↓
Docker
   ↓
Docker Compose
   ↓
Git
   ↓
GitHub
   ↓
GitHub Actions
   ↓
Dependabot
   ↓
Docker Image
   ↓
Amazon ECR
   ↓
AWS EC2
   ↓
CI/CD
   ↓
Terraform
   ↓
Kubernetes
   ↓
Amazon EKS
   ↓
Observabilidade
```

---

# 🏗️ Arquitetura Atual

Atualmente a aplicação possui dois containers principais:

```text
                    Docker Compose
                         │
             ┌───────────┴───────────┐
             │                       │
             ▼                       ▼
       ┌───────────┐          ┌────────────┐
       │  FastAPI  │          │ PostgreSQL │
       │           │─────────▶│            │
       │   :8000   │          │   :5432    │
       └───────────┘          └─────┬──────┘
                                    │
                                    ▼
                             postgres_data
```

### Componentes

**FastAPI**

Responsável pela API REST e pelos endpoints HTTP.

**PostgreSQL**

Responsável pela persistência dos dados.

**SQLAlchemy**

Responsável pela comunicação entre Python e PostgreSQL.

**Docker**

Responsável pela criação e execução dos containers.

**Docker Compose**

Responsável por orquestrar a API e o banco de dados localmente.

---

# 🛠️ Tecnologias

| Tecnologia     | Utilização                  |
| -------------- | --------------------------- |
| Python         | Linguagem principal         |
| FastAPI        | Framework da API            |
| Pydantic       | Validação dos dados         |
| SQLAlchemy     | ORM / comunicação com banco |
| PostgreSQL     | Banco de dados              |
| Pytest         | Testes automatizados        |
| Docker         | Containerização             |
| Docker Compose | Orquestração local          |
| Git            | Controle de versão          |
| GitHub         | Repositório remoto          |

---

# 📁 Estrutura do Projeto

```text
task-api/
│
├── .github/
│   └── workflows/
│       └── # CI será adicionado futuramente
│
├── tests/
│   ├── conftest.py
│   └── test_tasks.py
│
├── main.py
├── database.py
├── models.py
├── schemas.py
│
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
├── .env
├── requirements.txt
└── README.md
```

> O arquivo `.env` contém configurações locais e não deve ser versionado no Git.

---

# 🚀 Funcionalidades da API

A API possui operações básicas de gerenciamento de tarefas.

## Criar tarefa

```http
POST /tasks
```

Exemplo:

```json
{
  "title": "Estudar Docker",
  "description": "Aprender containers"
}
```

---

## Listar tarefas

```http
GET /tasks
```

Retorna todas as tarefas cadastradas.

---

## Buscar tarefa

```http
GET /tasks/{task_id}
```

Exemplo:

```http
GET /tasks/1
```

---

## Atualizar tarefa

```http
PUT /tasks/{task_id}
```

Exemplo:

```json
{
  "title": "Estudar Docker Compose",
  "completed": true
}
```

---

## Deletar tarefa

```http
DELETE /tasks/{task_id}
```

Exemplo:

```http
DELETE /tasks/1
```

---

# 📚 Documentação da API

O FastAPI gera automaticamente uma documentação interativa.

Com a aplicação rodando:

```text
http://localhost:8000/docs
```

Também existe a documentação OpenAPI:

```text
http://localhost:8000/redoc
```

---

# 💻 Executando Localmente

## 1. Clone o projeto

```bash
git clone <URL_DO_REPOSITORIO>
```

Entre na pasta:

```bash
cd task-api
```

---

## 2. Crie o ambiente virtual

Windows:

```powershell
python -m venv venv
```

Linux/macOS:

```bash
python3 -m venv venv
```

---

## 3. Ative o ambiente virtual

Windows PowerShell:

```powershell
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

---

## 4. Instale as dependências

```bash
pip install -r requirements.txt
```

---

# 🐘 PostgreSQL + Docker Compose

A forma recomendada de executar o projeto atualmente é utilizando Docker Compose.

Execute:

```bash
docker compose up --build
```

Para executar em segundo plano:

```bash
docker compose up -d --build
```

Verificar os containers:

```bash
docker compose ps
```

Ver os logs:

```bash
docker compose logs
```

Logs somente da API:

```bash
docker compose logs api
```

Logs somente do PostgreSQL:

```bash
docker compose logs db
```

Parar os containers:

```bash
docker compose down
```

---

# 🐳 Docker

A aplicação possui um `Dockerfile` próprio.

Para criar a imagem:

```bash
docker build -t task-api:1.0 .
```

Ver as imagens:

```bash
docker images
```

Executar o container:

```bash
docker run -d \
  -p 8000:8000 \
  --name task-api-container \
  task-api:1.0
```

Verificar:

```bash
docker ps
```

Logs:

```bash
docker logs task-api-container
```

---

# 🧪 Testes

O projeto possui testes automatizados utilizando **Pytest**.

Para executar:

```bash
pytest
```

Os testes verificam, entre outras coisas:

* funcionamento da rota principal;
* criação de tarefas;
* busca de tarefas;
* tratamento de tarefas inexistentes;
* códigos HTTP retornados;
* conteúdo das respostas.

Exemplo de resultado esperado:

```text
4 passed
```

---

# 🔐 Configuração e Variáveis de Ambiente

As configurações do PostgreSQL são fornecidas através de variáveis de ambiente.

Exemplo:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=tasks
```

A aplicação utiliza:

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/tasks
```

Credenciais e informações sensíveis **não devem ser commitadas no Git**.

Por isso o `.env` está incluído no `.gitignore`.

Em ambientes de produção, será utilizado um sistema apropriado de gerenciamento de secrets.

---

# 🔄 Fluxo Atual de Desenvolvimento

Atualmente o fluxo é:

```text
Desenvolvimento
      ↓
Python / FastAPI
      ↓
Testes com Pytest
      ↓
Docker Build
      ↓
Docker Compose
      ↓
PostgreSQL
      ↓
Git
      ↓
GitHub
```

---

# 🚧 Roadmap DevOps

## Fase 1 — Aplicação

* [x] Python
* [x] FastAPI
* [x] API REST
* [x] CRUD
* [x] Pydantic

---

## Fase 2 — Banco de Dados

* [x] SQLAlchemy
* [x] PostgreSQL
* [x] Persistência dos dados
* [x] Docker Volume

---

## Fase 3 — Qualidade

* [x] Pytest
* [x] Testes de endpoints
* [x] Testes de respostas HTTP

### Próximas melhorias

* [ ] Melhorar cobertura dos testes
* [ ] Banco de teste isolado
* [ ] Fixtures
* [ ] Testes de integração

---

## Fase 4 — Containers

* [x] Dockerfile
* [x] Docker Image
* [x] Docker Container
* [x] Docker Compose
* [x] Docker Network
* [x] Docker Volume
* [x] `.dockerignore`
* [x] Variáveis de ambiente

### Próximas melhorias

* [ ] Healthcheck
* [ ] Docker image otimizada
* [ ] Multi-stage build
* [ ] Usuário não-root no container
* [ ] Melhorias de segurança da imagem

---

# 🔄 Fase 5 — CI com GitHub Actions

**Próxima etapa.**

Objetivo:

```text
git push
   ↓
GitHub
   ↓
GitHub Actions
   ↓
Instalar dependências
   ↓
Executar Pytest
   ↓
Resultado
```

Será implementado:

* [ ] Primeiro workflow
* [ ] GitHub Actions
* [ ] Runner Linux
* [ ] Checkout do código
* [ ] Setup Python
* [ ] Instalação das dependências
* [ ] Execução dos testes
* [ ] Status da pipeline

Depois:

```text
GitHub Actions
      ↓
Pytest
      ↓
Docker Build
```

---

# 🔐 Fase 6 — Segurança

Após a CI básica:

* [ ] Dependabot
* [ ] Atualização automática de dependências
* [ ] GitHub Secrets
* [ ] Scan de dependências
* [ ] Scan da imagem Docker
* [ ] Princípio do menor privilégio
* [ ] Melhor gerenciamento de secrets

---

# 📦 Fase 7 — Container Registry

Próximo estágio da infraestrutura:

```text
GitHub Actions
      ↓
Docker Build
      ↓
Docker Image
      ↓
Amazon ECR
```

Será implementado:

* [ ] AWS IAM
* [ ] ECR Repository
* [ ] Login do Docker no ECR
* [ ] Tag da imagem
* [ ] Push da imagem
* [ ] Versionamento das imagens

---

# ☁️ Fase 8 — AWS EC2

Depois do ECR:

```text
ECR
 ↓
EC2
 ↓
Docker
 ↓
Task API
```

Será implementado:

* [ ] Criar EC2
* [ ] Configurar Security Group
* [ ] Configurar SSH
* [ ] Instalar Docker
* [ ] Autenticar no ECR
* [ ] Baixar imagem
* [ ] Executar container
* [ ] Disponibilizar API

---

# 🔁 Fase 9 — CI/CD

Objetivo:

```text
Developer
    │
    ▼
git push
    │
    ▼
GitHub
    │
    ▼
GitHub Actions
    │
    ├── Testes
    │
    ├── Build Docker
    │
    ├── Security Checks
    │
    ├── Push ECR
    │
    └── Deploy
          │
          ▼
         EC2
```

Será implementado:

* [ ] CI
* [ ] Build automático
* [ ] Push automático para ECR
* [ ] Deploy automático
* [ ] Secrets no GitHub
* [ ] Estratégia de rollback

---

# 🏗️ Fase 10 — Infrastructure as Code

A infraestrutura inicialmente criada manualmente será posteriormente automatizada.

Tecnologia planejada:

```text
Terraform
```

Será implementado:

* [ ] Terraform
* [ ] AWS Provider
* [ ] VPC
* [ ] Subnets
* [ ] Security Groups
* [ ] EC2
* [ ] ECR
* [ ] IAM
* [ ] Outputs
* [ ] Variables
* [ ] State

Objetivo:

```text
Código Terraform
       ↓
Terraform Plan
       ↓
Terraform Apply
       ↓
AWS Infrastructure
```

---

# ☸️ Fase 11 — Kubernetes

Depois de dominar Docker e Cloud:

```text
Docker
   ↓
Kubernetes
   ↓
EKS
```

Conceitos planejados:

* [ ] Pods
* [ ] Deployments
* [ ] Services
* [ ] ConfigMaps
* [ ] Secrets
* [ ] Namespaces
* [ ] Ingress
* [ ] Probes
* [ ] Resource Limits
* [ ] Horizontal Pod Autoscaler
* [ ] Kubernetes Security

Posteriormente:

```text
AWS EKS
```

---

# 📊 Fase 12 — Observabilidade

A aplicação também será evoluída para possuir observabilidade.

Planejado:

* [ ] Health checks
* [ ] Application logs
* [ ] Container logs
* [ ] Métricas
* [ ] Prometheus
* [ ] Grafana
* [ ] Alertas
* [ ] Monitoramento da infraestrutura

---

# 🎯 Objetivo Final

Ao final do projeto, a arquitetura planejada será aproximadamente:

```text
                         GitHub
                            │
                            │ Push
                            ▼
                   GitHub Actions
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
           Pytest                    Security Checks
              │                           │
              └─────────────┬─────────────┘
                            │
                            ▼
                       Docker Build
                            │
                            ▼
                       Docker Image
                            │
                            ▼
                       Amazon ECR
                            │
                            ▼
                         AWS EKS
                            │
              ┌─────────────┼─────────────┐
              │             │             │
              ▼             ▼             ▼
             API        PostgreSQL    Observability
              │                           │
              │                           ├── Prometheus
              │                           └── Grafana
              │
              ▼
           End Users
```

A infraestrutura será posteriormente gerenciada como código utilizando **Terraform**.

---

# 📖 O que este projeto demonstra

Este projeto tem como objetivo demonstrar conhecimentos práticos em:

* Desenvolvimento de APIs REST
* Python
* FastAPI
* Banco de dados relacional
* PostgreSQL
* SQLAlchemy
* Testes automatizados
* Docker
* Docker Compose
* Containers
* Redes Docker
* Volumes
* Variáveis de ambiente
* Git
* GitHub
* CI/CD
* GitHub Actions
* Dependency Management
* AWS
* ECR
* EC2
* IAM
* Terraform
* Kubernetes
* EKS
* Observabilidade

---

# 🧑‍💻 Status

**Projeto em desenvolvimento.**

A infraestrutura será construída progressivamente para demonstrar a evolução de uma aplicação simples para uma arquitetura DevOps completa.

Cada etapa do projeto será documentada para registrar **o problema, a solução, a tecnologia utilizada e os conceitos aprendidos**.

---

## 📌 Próxima etapa

```text
GitHub Actions
      ↓
CI
      ↓
Pytest automático
      ↓
Docker Build automático
```

**Status atual:** 🟢 Docker + PostgreSQL + Pytest + Git/GitHub concluídos.

**Próximo objetivo:** 🔵 construir a primeira pipeline de CI com GitHub Actions.
