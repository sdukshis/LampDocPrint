from django.test import TestCase, Client
from django.contrib.auth.models import User

# Create your tests here.

class LoginTestCase(TestCase):
    USER = 'bob'
    PASS = 'rob'

    def setUp(self):
        bob = User.objects.create_user(self.USER, '', self.PASS)
        bob.save()

    def test_redirect_to_login_page(self):
        c = Client()
        response = c.get('/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain, 
                        [('http://testserver/accounts/login/?next=/', 302)])

    def test_login_wrong_password(self):
        c = Client()
        response = c.post('/accounts/login/', {'username': 'bob',
                                               'password': 'wrong password'})

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.content.find('alert-danger'), -1)

    def test_login_correct_password(self):
        c = Client()
        response = c.post('/accounts/login/', {'username': self.USER,
                                               'password': self.PASS},
                                              follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain, 
                        [('http://testserver/', 302)])

        self.assertEqual(response.content.find('alert-danger'), -1)



