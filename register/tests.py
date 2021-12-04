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

   def logout(self):
       """tests for logout"""
       self.client.login(username='XXX', password="XXX") # Log in
       response = self.client.get('/admin/login')
       self.assertEquals(response.status_code, 200)# Check response code
       self.assertTrue('logout' in response.content)  # Check 'logout' in response
       self.client.logout() # Logout
       response = self.client.get('/admin/')
       self.assertEquals(response.status_code, 200) # Check response code
       self.assertTrue('signin' in response.content) # Check 'Log in' in response

   def test_update_profile(self):
       """tests for update_profile"""
       test_user = User.objects.create_user(username="user", password="123456")  # create a user
       author1 = Author.objects.create(user=test_user, fullname="test1", slug="user1",bio="just for test")  # create an author
       self.assertEqual(Author.objects.filter(fullname="test1").count(),1)  # after updating his fullname count authors with the name test1 should be 1