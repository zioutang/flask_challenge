
import requests
import unittest


class FlaskrTestCase(unittest.TestCase):

    def test1(self):
        response = requests.post('https://morning-dusk-64545.herokuapp.com/upload/1.png');
        # self.response = requests.post('/upload/IMG_2342.JPG', follow_redirects=True)
        self.assertEqual(response.status_code, 200);
    def test2(self):
        response = requests.post('https://morning-dusk-64545.herokuapp.com/upload/2.png');
        # self.response = requests.post('/upload/IMG_2342.JPG', follow_redirects=True)
        self.assertEqual(response.status_code, 200);
    def test3(self):
        response = requests.post('https://morning-dusk-64545.herokuapp.com/upload/3.jpg');
        # self.response = requests.post('/upload/IMG_2342.JPG', follow_redirects=True)
        self.assertEqual(response.status_code, 200);
    def test4(self):
        response = requests.post('https://morning-dusk-64545.herokuapp.com/upload/4.jpg');
        # self.response = requests.post('/upload/IMG_2342.JPG', follow_redirects=True)
        self.assertEqual(response.status_code, 200);

if __name__ == '__main__':
    unittest.main()
