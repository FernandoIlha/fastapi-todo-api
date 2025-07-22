import fastapi
import sqlite3
from pydantic import BaseModel
app = fastapi.FastAPI()

##banco de dados
conn = sqlite3.connect('tarefas.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT NOT NULL,
    concluida BOOLEAN NOT NULL CHECK (concluida IN (0, 1))
)''')


##Modelo Pydantic
class Tarefa(BaseModel):
    titulo: str
    descricao: str
    concluida: bool


##fucoes_app
@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    cursor.execute('INSERT INTO tarefas (titulo, descricao, concluida) VALUES (?, ?, ?)', (tarefa.titulo, tarefa.descricao, tarefa.concluida))
    conn.commit()
    return {"message": "Tarefa criada com sucesso!"}

@app.get("/tarefas")
def listar_tarefas():
    cursor.execute('SELECT * FROM tarefas')
    tarefas = cursor.fetchall()
    return {"tarefas": tarefas}

@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, titulo: str = None, descricao: str = None, concluida: bool = None):
   updates= []
   if titulo:
       updates.append(f"titulo = '{titulo}'")
   if descricao:
       updates.append(f"descricao = '{descricao}'")
   if concluida is not None:
       updates.append(f"concluida = {1 if concluida else 0}")
   if updates:
       cursor.execute(f"UPDATE tarefas SET {', '.join(updates)} WHERE id = ?", (tarefa_id,))
       conn.commit()
       return {"message": "Tarefa atualizada com sucesso!"}
   return {"message": "Nenhuma atualização realizada."}

@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int):
   cursor.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
   conn.commit()
   return {"message": "Tarefa deletada com sucesso!"}

