from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int
    name: str
    description: str
    status: Optional[str] = "Не завершена"


tasks: list[Task] = []


@app.get("/tasks/")
async def get_tasks():
    return tasks


@app.get("/tasks/{id}")
async def get_task(task_id: int):
    task = [task for task in tasks if task.id == task_id][0]
    return task


@app.post("/tasks")
async def create_task(task: Task):
    tasks.append(task)
    return task


@app.put("/tasks/{id}")
async def get_task(task_id: int, new_task:Task):
    task = [task for task in tasks if task.id == task_id][0]
    task.name = new_task.name
    task.description = new_task.description
    task.status = new_task.status
    return task


@app.delete("/tasks/{id}")
async def delete_task(task_id: int):
    task = [task for task in tasks if task.id == task_id][0]
    tasks.remove(task)
    return task

