from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Share
from rest_framework.test import APIClient

User = get_user_model()


class ConnectTestCase(TestCase):

    def setUp(self):  # formating(__init__) test database
        self.user = User.objects.create_user(
            username='beta', password="BETA!123")
        self.user_2 = User.objects.create_user(
            username='kilo', password="BETA!321")

        self.alfa = Share.objects.create(content="alfa", user=self.user)
        self.delta = Share.objects.create(content="delta", user=self.user_2)
        Share.objects.create(content="omega", user=self.user, parent=self.alfa)

        self.count = Share.objects.all().count()
        self.delta.likes.add(self.user, self.user_2)

    def apiclient(self):
        client = APIClient()
        client.login(username=self.user.username, password="BETA!123")
        return client

    def test_user_created(self):
        user = User.objects.get(username="beta")
        self.assertEqual(user.username, "beta")

    def test_Share_created(self):
        Share.objects.create(content="beta testing", user=self.user)
        qs = Share.objects.all()
        self.assertEqual(len(qs), 4)

    def test_list(self):
        client = APIClient()
        response = client.get('/api/share_ls')
        r_json = len(response.json())
        self.assertEqual(r_json, 3)
        self.assertEqual(response.status_code, 200)

    def test_action_and_detail(self):
        client = self.apiclient()
        response = client.post('/api/share/action',
                               {'id': 3, 'action': 'like'})
        self.assertEqual(response.status_code, 200)
        response = client.get('/api/share/3')
        self.assertEqual(response.status_code, 200)
        like = response.json()['likes']
        self.assertEqual(like, 1)

    def test_action_unlike(self):
        client = self.apiclient()
        response = client.post('/api/share/action',
                               {'id': "1", 'action': 'unlike'})
        self.assertEqual(response.status_code, 200)
        like = response.json()['likes']
        self.assertEqual(like, 0)

    def test_action_recommit(self):
        client = self.apiclient()
        response = client.post('/api/share/action',
                               {'id': "1", 'action': 'recommit'})
        response = client.post('/api/share/action',
                               {'id': "1", 'action': 'recommit'})
        response = client.post('/api/share/action',
                               {'id': "1", 'action': 'recommit'})
        response = client.post('/api/share/action',
                               {'id': "1", 'action': 'recommit'})
        self.assertEqual(response.status_code, 201)
        client = self.apiclient()
        response = client.get('/api/share_ls')
        r_json = len(response.json())
        self.assertEqual(r_json, 7)

    def test_API_share(self):
        client = self.apiclient()
        response = client.post('/api/share', {'content': 'Gamma'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'id': 4,
                                           'content': 'Gamma', 'likes': 0, 'user': 'beta', 'parent': None})

    def test_API_delete(self):
        client = self.apiclient()
        response = client.delete("/api/share/3/delete")
        self.assertEqual(len(Share.objects.all()), 2)
        self.assertEqual(response.status_code, 200)
        response = client.delete("/api/share/2/delete")
        self.assertEqual(response.json()[
                         'message'], 'You do not have permission for delete this commit')
        self.assertEqual(response.status_code, 401)
