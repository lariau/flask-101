# tests/test_views.py
from flask_testing import TestCase
from flask import jsonify
import json
from wsgi import app

class TestUpdate(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_update_product(self):
        fakedata = {"name": "newname"}
        response = self.client.patch("/api/v1/products/1", json=fakedata, content_type='application/json')
        self.assertEqual(response.status_code,204)
        print(response)
        #self.assertEqual(response.json['name'],'newname')

