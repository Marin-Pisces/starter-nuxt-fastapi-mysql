import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import get_connection
from pydantic import BaseModel

app = FastAPI()

frontend_url = os.getenv("FRONTEND_URL", "http://localhost:8090")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API is running!"}

# -----------------------------------------------------
# init
# -----------------------------------------------------
class Init(BaseModel):
    id: int
    text: str

@app.get("/init", response_model=list[Init])
def read_users():
    sql = "SELECT * FROM init"

    with get_connection() as (cursor, con):
        cursor.execute(sql)
        return cursor.fetchall()