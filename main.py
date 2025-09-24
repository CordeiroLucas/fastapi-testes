from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()
app.title = "API de Produtos"
app.version = "0.1.0"
app.description = "API para gerenciar produtos."

class Produto(BaseModel):
    id: UUID
    nome: str = Field(min_length=2, max_length=100)
    descricao: str = Field(min_length=5, max_length=300)

produtos = []

@app.get("/")
def listar_produtos():
    return produtos

@app.post("/")
def adicionar_produto(produto: Produto):
    produtos.append(produto)
    return produto

@app.put("/{produto_id}")
def atualizar_produto(produto_id: UUID, produto: Produto):
    for idx, p in enumerate(produtos):
        if p.id == produto_id:
            produtos[idx] = produto
            return produto
    raise HTTPException(status_code=404, detail=f"ID {produto_id} não encontrado")

@app.delete("/{produto_id}")
def deletar_produto(produto_id: UUID):
    for idx, p in enumerate(produtos):
        if p.id == produto_id:
            del produtos[idx]
            return {"detail": f"Produto com ID {produto_id} deletado"}
    raise HTTPException(status_code=404, detail=f"ID {produto_id} não encontrado")