from dotenv import load_dotenv
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2

app = FastAPI()
load_dotenv()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


class Task(BaseModel):
    title: str


@app.get("/")
def home():
    return {"message": "TaskFlow backend is running"}


@app.get("/tasks")
def get_tasks():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, title, completed FROM tasks ORDER BY id"
    )

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return [
        {
            "id": row[0],
            "title": row[1],
            "completed": row[2]
        }
        for row in rows
    ]


@app.post("/tasks")
def create_task(task: Task):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO tasks (title)
        VALUES (%s)
        RETURNING id, title, completed
        """,
        (task.title,)
    )

    row = cursor.fetchone()

    connection.commit()

    cursor.close()
    connection.close()

    return {
        "id": row[0],
        "title": row[1],
        "completed": row[2]
    }


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = %s",
        (task_id,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return {"message": "Task deleted"}
@app.put("/tasks/{task_id}/complete")
def complete_task(task_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET completed = NOT completed
        WHERE id = %s
        RETURNING id, title, completed
        """,
        (task_id,)
    )

    row = cursor.fetchone()

    connection.commit()

    cursor.close()
    connection.close()

    if row is None:
        return {"message": "Task not found"}

    return {
        "id": row[0],
        "title": row[1],
        "completed": row[2]
    }