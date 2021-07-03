from django.http import response
from django.test import TestCase
from .models import Profile
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User=get_user_model()


class TestCase(TestCase):
   
    def setUp(self):
        self.user = User.objects.create_user(
            username='beta', password="BETA!123")
        self.user_2 = User.objects.create_user(
            username='kilo', password="BETA!321")

    def apiclient(self):
        client = APIClient()
        client.login(username=self.user.username, password="BETA!123")
        return client
    
    
    def test_profile_created(self):
        qs = Profile.objects.all()
        self.assertEqual(qs.count(),2)


    def test_following(self):
        first=self.user
        second=self.user_2
        first.profile.followers.add(second)
        following_whom  =second.following.all()
        qs=following_whom.filter(user=first)
        following_no_one=first.following.all()
        self.assertTrue(qs.exists())
        self.assertFalse(following_no_one.exists())

    def test_follow_api_endpoint(self):
        client=self.apiclient()
        response=client.post(f'/api/profiles/{self.user_2.username}/follow',
        {"action":"follow"})
        r_data = response.json()
        count = r_data.get("count")
        self.assertEqual(count,1) 
        #unfollow
        response=client.post(f'/api/profiles/{self.user_2.username}/follow',
        {"action":"unfollow"})
        r_data = response.json()
        count = r_data.get("count")
        self.assertEqual(count,0) 
    
    def test_cannot_follow_api_endpoint(self):
        client=self.apiclient()
        response=client.post(f'/api/profiles/{self.user.username}/follow',
        {"action":"follow"})
        r_data = response.json()
        count = r_data.get("count")
        self.assertEqual(count,0) 
       