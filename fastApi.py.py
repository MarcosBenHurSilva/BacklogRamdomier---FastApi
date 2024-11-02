from fastapi import FastAPI, HTTPException
from random import choice

app = FastAPI()

# Lista para armazenar os backlogs
backlogs = {}


@app.post("/backlogs/{backlog_id}")
async def create_backlog(backlog_id: str, items: list[str]):
    """Cria um novo backlog com os itens fornecidos."""
    backlogs[backlog_id] = items
    return {"message": "Backlog criado com sucesso"}


@app.get("/backlogs/{backlog_id}/random")
async def get_random_item(backlog_id: str):
    """Retorna um item aleatório do backlog."""
    if backlog_id not in backlogs:
        raise HTTPException(status_code=404, detail="Backlog não encontrado")
    items = backlogs[backlog_id]
    if not items:
        raise HTTPException(status_code=404, detail="Backlog vazio")
    return {"item": choice(items)}
