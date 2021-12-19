from django.test import TestCase,Client
from django.contrib.auth import get_user_model
from .models import Profile, Skill

User = get_user_model()

class main_Test_Cases(TestCase):
   def setUp(self):
      #The test client is a Python class that acts as a dummy web browser, allowing you to test your views and interact with your Django-powered application programmatically.
      self.client = Client()

   def test_Profile(self):
      """tests for profiles"""
      test_user = User.objects.create_user(username="user", email="email@mail.com", password="123456") #create a user
      test_user2 = User.objects.create_user(username="user2", email="email2@mail.com", password="123456") #create a user
      self.assertEqual(Profile.objects.all().count(), 0) #count Profiles in the db should be 0
      profile1 = Profile.objects.create(user=test_user, name="test1", email="email@mail.com", username="test_user", location="here", short_intro="hi", bio="test profile") #create a Profile
      self.assertEqual(Profile.objects.all().count(), 1) #count Profile in the db should be 1
      profile2 = Profile.objects.create(user=test_user2, name="test2", email="email@mail.com", username="test_user2", location="there", short_intro="hi", bio="test profile2") #create a Profile
      self.assertEqual(Profile.objects.all().count(), 2) #count profiles in the db should be 2
      self.assertEqual(Profile.objects.filter(name="test1").count(), 1) #count profiles with the name test1 should be 1
      profile1.delete() #delete the profiles
      self.assertEqual(Profile.objects.filter(name="test1").count(), 0) #count profiles with the name test1 should be 0
      self.assertEqual(Profile.objects.all().count(), 1) #count profiles in the db should be 0

      #test if the profile2 has its own page
      #response = self.client.get('/users/profile/<str:pk>/')#get the address of this post page
      #self.assertEqual(response.status_code, 200)#check if the page exits or there is an error
      #self.assertTemplateUsed(response, 'users/guide-profile.html')#checks that the template with the given name was used in rendering the response
      #self.assertContains(response, 'test profile2')#test if test post content appers on the page

   def test_Skill(self):
      """tests for skills"""
      test_user = User.objects.create_user(username="user", email="email@mail.com", password="123456")  # create a user
      profile1 = Profile.objects.create(user=test_user, name="test1", email="email@mail.com", username="test_user",location="here", short_intro="hi", bio="test profile")  # create a Profile
      self.assertEqual(Skill.objects.all().count(), 0) #count Skills in the db should be 0
      skill1 = Skill.objects.create(owner=profile1, name="myskill1", description="test")  # create a skill
      self.assertEqual(Skill.objects.all().count(), 1) #count Skills in the db should be 1
      skill2 = Skill.objects.create(owner=profile1, name="myskill2", description="test2")  # create a skill
      self.assertEqual(Skill.objects.all().count(), 2) #count Skills in the db should be 2
      self.assertEqual(Skill.objects.filter(name="myskill1").count(), 1) #count skills with the name test1 should be 1
      skill2.delete() #delete the profiles
      self.assertEqual(Skill.objects.filter(name="myskill2").count(), 0) #count skills with the name test1 should be 0
      self.assertEqual(Skill.objects.all().count(), 1) #count skills in the db should be 0

