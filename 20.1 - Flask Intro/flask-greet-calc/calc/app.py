from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_nums():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    result = add(a, b)
    return str(result)
    
@app.route('/sub')
def subtract_nums():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def multiply_nums():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    result = mult(a, b)
    return str(result)

@app.route('/div')
def divide_nums():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    result = div(a, b)
    return str(result)