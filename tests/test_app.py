import unittest
from app import app, db
from models import License

class LicenseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Create a test license
        db.create_all()
        test_license = License(key="TEST123", product_id="SaaS-Test", status="inactive")
        db.session.add(test_license)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_validate_license(self):
        response = self.app.post('/license/validate', json={"license_key": "TEST123"})
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'License invalid or inactive')

    def test_activate_license(self):
        response = self.app.post('/license/activate', json={"license_key": "TEST123"}, headers={"Authorization": "Bearer <your_token>"})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'License activated successfully')

if __name__ == '__main__':
    unittest.main()
