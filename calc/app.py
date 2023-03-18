import operations
from flask import Flask, request
app = Flask(__name__)

@app.route('/math/<operation>')
def add(operation):
    
    a = int(request.args["a"])
    b = int(request.args["b"])
    if operation == "add":
        answer = operations.add(a,b)
    elif operation == "sub":
        answer = operations.sub(a,b)
    elif operation == "mult":
        answer = operations.mult(a,b)
    elif operation == "div":
        answer = operations.div(a,b)
    return f"{answer}"
