# wsgi.py
from flask import Flask, jsonify, request, Response
app = Flask(__name__)

PRODUCTS = [
    { 'id': 1,  'name': 'Skello' },
    { 'id': 2,  'name': 'Socialive.tv' },
    { 'id': 3,  'name': 'another.org'},
    { 'id': 12, 'name': 'yet-another.org'}
]

@app.route('/')
def hello():
    return "Hello World!!!!"

@app.route('/api/v1/products')
def products():
    return jsonify(PRODUCTS)

@app.route('/api/v1/products/<int:id>')
def product(id):
    if request.method == 'GET':
        for elem in PRODUCTS:
            if elem['id'] == id:
                return jsonify(elem)
        content = {'id': 'unknown'}
        return Response(content, status=404, mimetype='application/json')
    elif request.method == 'DELETE':
        pass
    elif request.method == 'PATCH':
        pass
    elif request.method == 'POST':
        pass

