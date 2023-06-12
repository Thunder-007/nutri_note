from django.test import TestCase, SimpleTestCase
from django.urls import reverse


# Create your tests here.
class HelloTest(SimpleTestCase):

    def test_http_response(self):
        url = reverse('hello_world')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content.decode(), "Hello World")
