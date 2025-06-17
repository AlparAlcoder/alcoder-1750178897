# Wedding Task Manager API Documentation

This is a simple FastAPI application that is designed to manage wedding tasks. It provides endpoints to create, retrieve, update, and delete tasks. Each task has an id, name, and a completed status.

## Dependencies
- FastAPI: a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- Pydantic: a data validation library that uses Python type annotations to validate data and serialize/deserialize to/from JSON.

## Models

### Task
Defines the structure of a task.
```python
class Task(BaseModel):
    id: Optional[int]
    name: str
    completed: bool
```

## Endpoints

### GET /tasks
Retrieve all wedding tasks.

**Response Model:** List[Task]

**Examples:** `curl -X GET http://localhost:8000/tasks` 

### GET /tasks/{task_id}
Retrieve a specific wedding task by its id.

**Parameters:**

- `task_id` (int) : The id of the task to retrieve.

**Response Model:** Task

**Examples:** `curl -X GET http://localhost:8000/tasks/1`

### POST /tasks
Create a new wedding task.

**Parameters:**

- `task` (Task) : The task to create.

**Response Model:** Task

**Examples:** `curl -X POST http://localhost:8000/tasks -d '{"name": "Buy flowers", "completed": false}'`

### PUT /tasks/{task_id}
Update an existing wedding task.

**Parameters:**

- `task_id` (int) : The id of the task to update.
- `task` (Task) : The updated task.

**Response Model:** Task

**Examples:** `curl -X PUT http://localhost:8000/tasks/1 -d '{"name": "Buy flowers", "completed": true}'`

### DELETE /tasks/{task_id}
Delete a wedding task.

**Parameters:**

- `task_id` (int) : The id of the task to delete.

**Examples:** `curl -X DELETE http://localhost:8000/tasks/1`

## Important Notes
- All task operations are done in memory, there is no database in this application. If you restart the application, all data will be lost.
- The `id` field is optional when creating a new task. If not provided, FastAPI will automatically assign a unique id to the task.
- If a task is not found for the id provided in the GET, PUT and DELETE operations, a 404 HTTPException will be raised with a detail message "Task not found".