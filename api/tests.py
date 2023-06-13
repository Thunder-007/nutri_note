from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import DiveUser


# Create your tests here.
class HelloTest(SimpleTestCase):

    def test_http_response(self):
        url = reverse('hello_world')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content.decode(), "Hello World")


class TestUserRegistration(TestCase):

    def setUp(self) -> None:
        pass

    def test_duplicate_user(self):
        url = reverse('register')
        DiveUser.objects.create(username='username', password='1234', email='email@email.com').save()
        response = self.client.post(url, data={
            'username': 'username',
            'email': 'username@harsha07.tech',
            'password': '1234'
        })
        self.assertNotEquals(response.status_code, 201)

    def test_user_creation(self):
        url = reverse('register')
        response = self.client.post(url, data={
            'username': 'username',
            'email': 'username@harsha07.tech',
            'password': '1234'
        })
        self.assertEquals(response.status_code, 201)
