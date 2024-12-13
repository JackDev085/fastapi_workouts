from fastapi import FastAPI
from src.repository.WorkoutRepository import WorkoutRepository
from src.db.connection import Connection
from fastapi.middleware.cors import CORSMiddleware

#APP
app = FastAPI(title="Workouts API")

origins = [
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5500"
    "http://127.0.0.1:8080",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8081",
    "http://127.0.0.1",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



#Repositório de conexão com banco de dados para a tabela treinos
conn = Connection("db.sqlite3")
workout_repository = WorkoutRepository(cursor=conn)

@app.get("/")
async def hello_world():
    return {"message": "hello world"}

@app.get("/treinos")
async def all_workouts():
    workouts = workout_repository.fetch_all()
    return workouts

@app.get("/treinos/{id}")
async def fetch_one(id:int):
    workout = workout_repository.fetch_one(id)
    return workout

"""@app.get("/treinos/category/{category}")
async def fetch_by_category(category:str):
    workout = workout_repository.fetch_by_category(category)
    if len(workout) < 1:
        return {"message":"Nenhum treino para essa categoria"}
    return workout"""