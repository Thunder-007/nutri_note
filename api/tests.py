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


class UserRegistration(TestCase):

    def test_duplicate_user(self):
        url = reverse('register')
        DiveUser.objects.create(username='username1', password='1234', email='username1@email.com').save()
        response = self.client.post(url, data={
            'username': 'username1',
            'email': 'username@harsha07.tech',
            'password': '1234'
        })
        self.assertNotEquals(response.status_code, 201)

    def test_user_creation(self):
        url = reverse('register')
        response = self.client.post(url, data={
            'username': 'username',
            'email': 'username1@harsha07.tech',
            'password': '1234'
        })
        self.assertEquals(response.status_code, 201)


class UserLogin(TestCase):
    def test_user_login(self):
        url = reverse('login')
        DiveUser.objects.create_user(username='username', password='1234', email='useer@usermail.com')
        response = self.client.post(url, data={
            'username': 'username',
            'password': '1234',
        })
        self.assertEquals(response.status_code, 200)


class UserLogout(TestCase):
    def test_user_logout(self):
        login_url = reverse('login')
        DiveUser.objects.create_user(username='username', password='1234')
        login_response = self.client.post(login_url, data={
            'username': 'username',
            'password': '1234',
        })
        logout_url = reverse('logout')
        logout_response = self.client.post(logout_url, headers={
            'Authorization': f'Token {login_response.json()["token"]}'
        })
        self.assertEquals(logout_response.status_code, 200)


class CrudUsers(TestCase):
    def test_manager_can_crud(self):
        # Test Manager
        manager_url = reverse('manage_users')
        login_url = reverse('login')
        DiveUser.objects.create_user(username='moderator', password='1234', level='moderator')
        login_response = self.client.post(login_url, data={
            'username': 'moderator',
            'password': '1234',
        })
        manager_response = self.client.get(manager_url, headers={
            'Authorization': f'Token {login_response.json()["token"]}'
        })
        self.assertEquals(manager_response.status_code, 200)
        # Test General Users
        DiveUser.objects.create_user(username='user', password='1234', email='newuser@email.com', level='user')
        login_response = self.client.post(login_url, data={
            'username': 'user',
            'password': '1234',
        })
        manager_response = self.client.get(manager_url, headers={
            'Authorization': f'Token {login_response.json()["token"]}'
        })
        self.assertEquals(manager_response.status_code, 403)


class CrudUser(TestCase):
    def test_get_destroy_user(self):
        login_url = reverse('login')
        DiveUser.objects.create_user(username='usieer', password='1234', email='thisuser@mail.com', level='user')
        DiveUser.objects.create_user(username='moderator', password='1234', level='moderator')
        login_response = self.client.post(login_url, data={
            'username': 'moderator',
            'password': '1234',
        })
        pk = DiveUser.objects.get(username='usieer').pk
        user_url = reverse('manage_user', kwargs={'pk': pk})
        manager_response = self.client.delete(user_url, headers={
            'Authorization': f'Token {login_response.json()["token"]}'
        })
        try:
            DiveUser.objects.get(pk=pk)
            raise Exception("User not deleted")
        except DiveUser.DoesNotExist:
            self.assertEquals(True, True)
        self.assertEquals(manager_response.status_code, 200)
