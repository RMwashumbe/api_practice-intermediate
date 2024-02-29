import requests
from flask import Flask, jsonify, requests

app = Flask(__name__)

todos = []


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


app.route('/todos', methods=['POST'])


def add_todo():
    todo = requests.json
    todos.append(todo)
    return jsonify({"message": "Todo added successfully"})


if __name__ == "__main__":
    app.run(debug=True)
