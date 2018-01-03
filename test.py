# import os
# import flaskr
import requests
import unittest
# import tempfile
# import app

class FlaskrTestCase(unittest.TestCase):
    # def setUp(self):
    #     self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
    #     flaskr.app.testing = True
    #     self.app = flaskr.app.test_client()
    #     with flaskr.app.app_context():
    #         flaskr.init_db()
    #
    # def tearDown(self):
    #     os.close(self.db_fd)
    #     os.unlink(flaskr.app.config['DATABASE'])

    def test1(self):
        response = requests.post('http://localhost:3000/upload/1.png');
        # self.response = requests.post('/upload/IMG_2342.JPG', follow_redirects=True)
        self.assertEqual(response.status_code, 200);
    def test2(self):
        response = requests.post('http://localhost:3000/upload/2.png');
        # self.response = requests.post('/upload/IMG_2342.JPG', follow_redirects=True)
        self.assertEqual(response.status_code, 200);
    def test3(self):
        response = requests.post('http://localhost:3000/upload/3.jpg');
        # self.response = requests.post('/upload/IMG_2342.JPG', follow_redirects=True)
        self.assertEqual(response.status_code, 200);
    def test4(self):
        response = requests.post('http://localhost:3000/upload/4.jpg');
        # self.response = requests.post('/upload/IMG_2342.JPG', follow_redirects=True)
        self.assertEqual(response.status_code, 200);

if __name__ == '__main__':
    unittest.main()
