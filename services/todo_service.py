from readline import append_history_file
from tkinter import W
from services.dummy_data import get_todos, add_todo, edit_todo, delete_todo
from flask import Flask, jsonify, request, Response


app = Flask(__name__)

@app.route("/api/tasks", methods=['GET'])
def list_todos():
    return jsonify(get_todos())
    
@app.route("/api/tasks/<task>", methods=['POST', 'PUT'])
def add_todos(task):
    if request.method == 'PUT':
        edit_todo(task)
        return Response(status=200)
    if request.method == 'POST':
        add_todo(task)
        return Response(status=201)

@app.route("/api/tasks/<id>", methods=['DELETE'])
def edit_todos(task_id):
    delete_todo(task_id)
    return Response(status=200)

if __name__ == "__main__":
    app.run()