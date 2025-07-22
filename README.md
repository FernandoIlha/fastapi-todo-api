# API de Tarefas - FastAPI & SQLite

Este projeto é uma API simples para gerenciamento de tarefas (CRUD) desenvolvida com [FastAPI](https://fastapi.tiangolo.com/) e [SQLite](https://www.sqlite.org/index.html).

## Features Implementadas
- [x] CRUD completo de tarefas  
- [x] Banco de dados SQLite (pronto para migração para PostgreSQL)  
- [x] Proteção contra SQL Injection  
- [x] Documentação automática via Swagger  

## Tecnologias Usadas  
- Python 3.11  
- FastAPI  
- SQLite  
- Render (deploy)  

## Próximos Passos  
- [ ] Autenticação JWT  
- [ ] Dockerização  
- [ ] Testes automatizados com pytest

## Funcionalidades

- Criar tarefas
- Listar tarefas
- Atualizar tarefas
- Deletar tarefas

## Como executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seuusuario/seurepositorio.git](https://github.com/FernandoIlha/fastapi-todo-api
   cd seurepositorio
   ```

2. **Crie e ative um ambiente virtual (opcional):**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install fastapi uvicorn pydantic
   ```

4. **Execute o servidor:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Acesse a documentação interativa:**
   - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Endpoints

- `POST /tarefas` - Cria uma nova tarefa
- `GET /tarefas` - Lista todas as tarefas
- `PUT /tarefas/{tarefa_id}` - Atualiza uma tarefa existente
- `DELETE /tarefas/{tarefa_id}` - Deleta uma tarefa

## Como Testar via Curl

```bash
# Criar tarefa
curl -X POST "http://localhost:8000/tarefas" -H "Content-Type: application/json" -d '{"titulo":"Estudar FastAPI","descricao":"Praticar CRUD"}' 
```
## Estrutura da Tarefa

```json
{
  "titulo": "string",
  "descricao": "string",
  "concluida": true
}
```

## Autor

- Fernando Rodrigues Ilha https://www.linkedin.com/in/fernando-rodrigues-ilha-0669b2261/
---

