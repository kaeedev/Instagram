from django.test import TestCase
from profiles.models import UserProfile, Follow
from django.contrib.auth.models import User

class UserProfileModelTest(TestCase):

    def setUp(self):
        # cREAR USUARIO Y PERFIL
        self.user1 = User.objects.create_user(
            username='john',
            email='john@lennon.com',
            password='password123'
        )
        self.user2 = User.objects.create_user(
            username='paul',
            email='paul@mccarteny.com',
            password='password123'
        )
        self.profile1 = UserProfile.objects.create(
            user=self.user1,
            bio='im a musician',
            birth_date='1940-10-09'
        )
        self.profile2 = UserProfile.objects.create(
            user=self.user2,
            bio='im also a musician',
            birth_date='1942-06-18'
        )

    def test_user_profile_creation(self):
        self.assertEqual(self.profile1.bio, "im a musician")
        self.assertEqual(self.user1.username, 'john')

    def test_follow_user(self):
        self.profile1.follow(self.profile2)
        self.assertTrue(
            (Follow.objects.filter(follower=self.profile1, following=self.profile2).exists())
        )
    
    def test_unfollow_user(self):
        self.profile1.follow(self.profile2)
        self.assertTrue(
            (Follow.objects.filter(follower=self.profile1, following=self.profile2).exists())
        )
        self.profile1.unfollow(self.profile2)
        self.assertFalse(
            (Follow.objects.filter(follower=self.profile1, following=self.profile2).exists())
        )
        
    def test_str_userprofile(self):
        self.assertEqual(str(self.profile1), self.profile1.user.username)


class FollowModelTest(TestCase):

    def setUp(self):
        print('Ejecutando setup')
        # cREAR USUARIO Y PERFIL
        self.user1 = User.objects.create_user(
            username='john',
            email='john@lennon.com',
            password='password123'
        )
        self.user2 = User.objects.create_user(
            username='paul',
            email='paul@mccarteny.com',
            password='password123'
        )
        self.profile1 = UserProfile.objects.create(
            user=self.user1,
            bio='im a musician',
            birth_date='1940-10-09'
        )
        self.profile2 = UserProfile.objects.create(
            user=self.user2,
            bio='im also a musician',
            birth_date='1942-06-18'
        )
