from django.test import TestCase,Client
from django.contrib.auth import get_user_model,authenticate
from .forms import UpdateForm
from .views import signup,signin,update_profile,logout
from  forum.models import User,Author
from django.contrib.auth import logout as lt
from django.contrib.auth.decorators import login_required

User = get_user_model()

class main_Test_Cases(TestCase):
   def setUp(self):
      self.client = Client()

   def test_signup(self):
       """tests for signup"""
       test_user = User.objects.create_user(username="user",password="123456")  # create a user
       self.assertEqual(User.objects.all().count(), 1)  # count users in the db should be 1
       test_user.delete()  # delete the user
       self.assertEqual(User.objects.all().count(), 0)  # count Users in the db should be 0


   def test_update_profile(self):
       """tests for update_profile"""
       test_user = User.objects.create_user(username="user", password="123456")  # create a user
       author1 = Author.objects.create(user=test_user, fullname="test1", bio="just for test")  # create an author
       author1.fullname="changed"
       author1.save()
       self.assertEqual(Author.objects.filter(fullname="changed").count(),1)  # after updating his fullname count authors with the name test2 should be 1
       author1.delete()# delete the author
       self.assertEqual(Author.objects.all().count(), 0)  # count Authors in the db should be 0
       test_user.delete()  # delete the user
       self.assertEqual(User.objects.all().count(), 0)  # count Users in the db should be 0
