from readline import append_history_file
from services.dummy_data import get_todos, add_todo, edit_todo, delete_todo
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/api/tasks", methods=['GET'])
def list_todos():
    return jsonify(get_todos())
    
@app.route("/api/tasks/<task>", methods=['POST', 'PUT'])
def add_todos(task):
    if request.method == 'PUT':
        edit_todo(task)
    if request.method == 'POST':
        add_todo(task)
    return jsonify(get_todos())

@app.route("/api/tasks/<id>", methods=['DELETE'])
def edit_todos(task_id):
    delete_todo(task_id)
    return jsonify(get_todos())

if __name__ == "__main__":
    app.run()