from flask import Flask, request, render_template_string
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# In-memory data store with sample todos
TODOS = {
    1: {"task": "Buy groceries", "completed": False},
    2: {"task": "Finish Flask project", "completed": True},
    3: {"task": "Book doctor appointment", "completed": False},
    4: {"task": "Write blog post", "completed": False},
    5: {"task": "Plan vacation", "completed": True},
    6: {"task": "Read a new book", "completed": False},
    7: {"task": "Call plumber", "completed": True},
    8: {"task": "Clean the house", "completed": False},
}

# Request parser setup
parser = reqparse.RequestParser()
parser.add_argument(
    'task',
    type=str,
    required=True,
    help='Task description is required and must be a string.'
)

class TodoListResource(Resource):
    def get(self):
        return TODOS, 200

    def post(self):
        args = parser.parse_args()
        new_id = max(TODOS.keys(), default=0) + 1
        TODOS[new_id] = {"task": args["task"], "completed": False}
        return {new_id: TODOS[new_id]}, 201

class TodoResource(Resource):
    def get(self, todo_id):
        todo = TODOS.get(todo_id)
        if todo is None:
            return {"error": "Todo not found"}, 404
        return {todo_id: todo}, 200

    def delete(self, todo_id):
        if todo_id not in TODOS:
            return {"error": "Todo not found"}, 404
        del TODOS[todo_id]
        return '', 204

api.add_resource(TodoListResource, '/todos')
api.add_resource(TodoResource, '/todos/<int:todo_id>')

# Welcome Page at root '/'
@app.route('/')
def home():
    methods_colors = {
        'GET': '#28a745',    # green
        'POST': '#007bff',   # blue
        'DELETE': '#dc3545', # red
    }

    endpoints = [
        {'path': '/todos', 'methods': ['GET', 'POST'], 'desc': 'List all todos / Create a new todo'},
        {'path': '/todos/<int:todo_id>', 'methods': ['GET', 'DELETE'], 'desc': 'Get or delete a specific todo by ID'},
    ]

    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Flask RESTful Todo API</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px auto;
                max-width: 900px;
                color: #212529;
                line-height: 1.6;
                padding: 0 15px;
            }
            h1, h2, h3 {
                color: #343a40;
            }
            .method {
                font-weight: bold;
                padding: 2px 8px;
                border-radius: 4px;
                color: white;
                margin-right: 6px;
                font-family: monospace;
                font-size: 0.9em;
            }
            .GET { background-color: {{ methods_colors['GET'] }}; }
            .POST { background-color: {{ methods_colors['POST'] }}; }
            .DELETE { background-color: {{ methods_colors['DELETE'] }}; }
            code {
                background-color: #f8f9fa;
                padding: 2px 4px;
                border-radius: 3px;
                font-family: monospace;
            }
            a {
                color: #007bff;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 10px;
                margin-bottom: 40px;
            }
            th, td {
                border: 1px solid #dee2e6;
                padding: 8px 12px;
                text-align: left;
            }
            th {
                background-color: #e9ecef;
            }
            .completed {
                color: #28a745;
                font-weight: bold;
            }
            .pending {
                color: #dc3545;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <h1>Flask RESTful Todo API</h1>
        <p>This API allows you to manage a simple todo list with RESTful endpoints.</p>
        
        <h2>Available Endpoints</h2>
        <table>
            <thead>
                <tr>
                    <th>Endpoint</th>
                    <th>HTTP Methods</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                {% for ep in endpoints %}
                <tr>
                    <td><code>{{ ep.path }}</code></td>
                    <td>
                        {% for method in ep.methods %}
                        <span class="method {{ method }}">{{ method }}</span>
                        {% endfor %}
                    </td>
                    <td>{{ ep.desc }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>

        <h2>Example Usage</h2>
        <ul>
            <li><a href="{{ url_for('todolistresource') }}">GET /todos</a> - List all todos</li>
            <li><a href="{{ url_for('todolistresource') }}" onclick="event.preventDefault(); alert('Use POST with JSON {\"task\": \"new task\"}');">POST /todos</a> - Create a new todo</li>
            <li><a href="{{ url_for('todoresource', todo_id=1) }}">GET /todos/1</a> - Get todo with ID 1</li>
            <li><a href="{{ url_for('todoresource', todo_id=1) }}" onclick="event.preventDefault(); alert('Use DELETE to delete this todo');">DELETE /todos/1</a> - Delete todo with ID 1</li>
        </ul>
        
        <h2>Sample Todos</h2>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Task</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                {% for id, todo in todos.items() %}
                <tr>
                    <td>{{ id }}</td>
                    <td>{{ todo.task }}</td>
                    <td>
                        {% if todo.completed %}
                            <span class="completed">Completed</span>
                        {% else %}
                            <span class="pending">Pending</span>
                        {% endif %}
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        <footer>
            <p style="margin-top: 60px; font-size: 0.9em; color: #6c757d;">&copy; 2025 Flask RESTful Todo API</p>
        </footer>
    </body>
    </html>
    '''
    return render_template_string(html, todos=TODOS, endpoints=endpoints, methods_colors=methods_colors)

if __name__ == '__main__':
    app.run(debug=True)
