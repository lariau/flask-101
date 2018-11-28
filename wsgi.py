# wsgi.py
from flask import Flask, jsonify, request, Response
from counter import Counter
app = Flask(__name__)

PRODUCTS = [
    { 'id': 1,  'name': 'Skello' },
    { 'id': 2,  'name': 'Socialive.tv' },
    { 'id': 3,  'name': 'another.org'},
    { 'id': 12, 'name': 'yet-another.org'}
]

ID = Counter()

@app.route('/')
def hello():
    return "Hello World!!!!"

@app.route('/api/v1/products', methods = ['GET','POST'])
def products():
    if request.method == 'GET':
        return jsonify(PRODUCTS)
    elif request.method == 'POST':
        content = request.get_json()
        new_product = { "id": ID.next(), "name": content['name']}
        return Response(jsonify(new_product), status=201, mimetype='application/json')

@app.route('/api/v1/products/<int:id>', methods = ['GET','DELETE','PATCH'])
def product(id):
    if request.method == 'GET':
        for elem in PRODUCTS:
            if elem['id'] == id:
                return jsonify(elem)
        content = {f'id {id}': 'unknown'}
        return Response(content, status=404, mimetype='application/json')
    elif request.method == 'DELETE':
        for elem in PRODUCTS:
            if elem['id'] == id:
                return Response('', status=204, mimetype='application/json')
        content = {'unknown': 'unknown'}
        return Response(content, status=404, mimetype='application/json')
    elif request.method == 'PATCH':
        for elem in PRODUCTS:
            if elem['id'] == id:
                mycontent = {"id": id, "name": "dummy"}
                return jsonify(mycontent), 204
                #return Response(response=jsonify(mycontent), status=204, mimetype='application/json')

