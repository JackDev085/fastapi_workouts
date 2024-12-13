from fastapi import FastAPI
from src.repository.TreinosRepository import TreinosRepository
from src.db.connection import cursor

#APP
app = FastAPI(title="Workouts API")

#Repositório de conexão com banco de dados para a tabela treinos
workout_repository = TreinosRepository(cursor=cursor)

@app.get("/")
def hello_world():
    return {"message": "hello world"}

@app.get("/treinos")
def all_workouts():
    workouts = workout_repository.fetch_all()
    return workouts

@app.get("/treinos/{id}")
def fetch_one(id:int):
    workout = workout_repository.fetch_one(id)
    return workout

@app.get("/treinos/category/{category}")
def fetch_by_category(category:str):
    workout = workout_repository.fetch_by_category(category)
    if len(workout) < 1:
        return {"message":"Nenhum treino para essa categoria"}
    return workout