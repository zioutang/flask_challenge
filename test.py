
import requests
import unittest


class FlaskrTestCase(unittest.TestCase):

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
