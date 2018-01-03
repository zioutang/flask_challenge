
import requests
import unittest


class FlaskrTestCase(unittest.TestCase):

    def test1(self):
        files = {'file': open('images/1.png')}
        response = requests.post('https://morning-dusk-64545.herokuapp.com/upload',files=files);
        self.assertEqual(response.status_code, 200);
    def test2(self):
        files = {'file': open('images/2.png')}
        response = requests.post('https://morning-dusk-64545.herokuapp.com/upload',files=files);
        self.assertEqual(response.status_code, 200);
    def test3(self):
        files = {'file': open('images/3.JPG')}
        response = requests.post('https://morning-dusk-64545.herokuapp.com/upload',files=files);
        self.assertEqual(response.status_code, 200);
    def test4(self):
        files = {'file': open('images/4.JPG')}
        response = requests.post('https://morning-dusk-64545.herokuapp.com/upload',files=files);
        self.assertEqual(response.status_code, 200);

if __name__ == '__main__':
    unittest.main()
