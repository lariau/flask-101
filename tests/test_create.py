# tests/test_views.py
from flask_testing import TestCase
from flask import jsonify
import json
from wsgi import app

class TestCreate(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_create_new_product(self):
        fakedata = {"name": "Workelo"}
        response = self.client.post("/api/v1/products", json=fakedata, content_type='application/json')
        self.assertEqual(response.status_code,201)
        #self.assertEqual(response.json['name'],'Workelo')

