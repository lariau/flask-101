# tests/test_views.py
from flask_testing import TestCase
from wsgi import app

class TestDelete(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_delete_existing_product(self):
        response = self.client.delete("/api/v1/products/1")
        self.assertEqual(response.status_code,204)

    def test_delete_unkown_product(self):
        response = self.client.delete("/api/v1/products/5")
        self.assertEqual(response.status_code,404)
