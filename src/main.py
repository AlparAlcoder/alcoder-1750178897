from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

tasks = []


class Task(BaseModel):
    id: Optional[int]
    name: str
    completed: bool


@app.get('/tasks', response_model=List[Task])
async def get_tasks():
    """
    Retrieve all wedding tasks
    """
    return tasks


@app.get('/tasks/{task_id}', response_model=Task)
async def get_task(task_id: int):
    """
    Retrieve a specific wedding task
    """
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post('/tasks', response_model=Task)
async def create_task(task: Task):
    """
    Create a new wedding task
    """
    tasks.append(task)
    return task


@app.put('/tasks/{task_id}', response_model=Task)
async def update_task(task_id: int, task: Task):
    """
    Update an existing wedding task
    """
    for index, current_task in enumerate(tasks):
        if current_task.id == task_id:
            tasks[index] = task
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int):
    """
    Delete a wedding task
    """
    for index, current_task in enumerate(tasks):
        if current_task.id == task_id:
            tasks.pop(index)
            return {"message": "Task has been deleted successfully!"}
    raise HTTPException(status_code=404, detail="Task not found")