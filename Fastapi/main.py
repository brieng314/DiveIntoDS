from models import Todos
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}   

todos = []

#Get todos
@app.get("/todos")
async def get_todos():
    return {"todos":todos}

#get todos by id
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo":todo}
    return {"Message":"No todos are found"}

#post a todos
@app.post("/todos")
async def create_todos(todo_obj: Todos):
    todos.append(todo_obj)
    return {"messaage":"todos has been added"}

#update a todos
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_obj: Todos):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"todo":todo}
    return {"Message":"No todos are found to update"}

#Delete a todos
@app.delete("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"Message":"todo has been deleted"}
    return {"Message":"No todos are found"}

