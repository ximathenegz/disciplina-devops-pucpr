import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool


@app.get("/helloworld")
def root():
    return {"message": " Hello World"}


@app.get("/funcaoteste")
def funcaoteste():
    return {
        "teste": True,
        "num_aleatorio": random.randint(0, 57000)
    }


@app.post("/estudantes/cadastro")
def create_estudante(estudante: Estudante):
    return estudante


@app.put("/estudantes/update/{id_estudante}")
def update_estudante(id_estudante: int):
    return id_estudante > 0


@app.delete("/estudantes/delete/{id_estudante}")
def delete_estudante(id_estudante: int):
    return id_estudante > 0