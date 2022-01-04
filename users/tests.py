from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile, Skill, Review

User = get_user_model()

class main_Test_Cases(TestCase):

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
      profile1.delete() #delete the profile
      self.assertEqual(Profile.objects.filter(name="test1").count(), 0) #count profiles with the name test1 should be 0
      self.assertEqual(Profile.objects.all().count(), 1) #count profiles in the db should be 0


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

   def test_Review(self):
      """tests for Reviews"""
      test_user = User.objects.create_user(username="user", email="email@mail.com",password="123456")  # create a user
      test_user2 = User.objects.create_user(username="user2", email="email@mail.com",password="123456")  # create a user
      self.assertEqual(Review.objects.all().count(), 0)  # count Reviews in the db should be 0
      profile1 = Profile.objects.create(user=test_user, name="test1", email="email@mail.com", username="test_user",location="here", short_intro="hi", bio="test profile")  # create a Profile
      profile2 = Profile.objects.create(user=test_user2, name="test2", email="email@mail.com", username="test_user2",location="here", short_intro="hi", bio="test profile2")  # create a Profile
      VOTE_TYPE = (
         ('up', 'Up Vote'),
         ('down', 'Down Vote'),
         )
      review1 = Review.objects.create(owner=profile1, body="test1", value=VOTE_TYPE)
      self.assertEqual(Review.objects.all().count(), 1)  # count Reviews in the db should be 1
      review2 = Review.objects.create(owner=profile2, body="test2", value=VOTE_TYPE)
      self.assertEqual(Review.objects.all().count(), 2)  # count Reviews in the db should be 2
      self.assertEqual(Review.objects.filter(body="test1").count(),1)  # count Reviews with the name test1 should be 1
      review1.delete()  # delete the profiles
      self.assertEqual(Review.objects.filter(body="test1").count(),0)  # count Reviews with the name test1 should be 0
      self.assertEqual(Review.objects.all().count(), 1)  # count Reviews in the db should be 0

