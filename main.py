from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI(title= "TodoAPI")

class Todo(BaseModel):
  tehtava:str
  deadline : str
  kuvaus : Optional[str] = None

tehtävä_lista = []

@app.get('/')

async def home():
  return {"Hello": "World"}

@app.post('/Todo/')

async def todo(todo:Todo):
  tehtävä_lista.append(todo)
  return todo

@app.get('/Todo/', response_model = List[Todo])
async def kokolista():
  return tehtävä_lista

@app.get('/Todo/{id}')
async def get_todo(id : int):
  try:
    return tehtävä_lista[id]
  except: 
    raise HTTPException(status_code = 404, detail = "Todo not found")

@app.post('/Todo/{id}')

async def update_todo(id : int, todo : Todo):
  try:
    tehtävä_lista[id] = todo
    return tehtävä_lista[id]
  except: 
    raise HTTPException(status_code = 404, detail = "Todo not found")


@app.post('/Todo/')
async def lisaa_tehtava(todo:Todo):
  store_todo.append(todo)
  return todo

@app.put('/todo/{id}')
async def update_todo(id: int, todo: Todo):
    tehtävä_lista[id] = todo
    return tehtävä_lista[id]

@app.delete('/Todo/{id}')
async def poista(id : int):
  kohde = tehtävä_lista[id]
  tehtävä_lista.pop(id)
  return kohde
  