#database tabels

from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField
from tinymce.models import HTMLField
from taggit.managers import TaggableManager
from django.shortcuts import reverse
from django.contrib.auth.models import Group

User = get_user_model() #ready model for user imported from django.contrib.auth

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=40, blank=True)
    slug = models.SlugField(max_length=400, unique=True, blank=True) # imported from django.utils.text
    bio = HTMLField() #desctription of the user imported the field from tinymce.models

    #Display the name insted of "object 1" in the admin page
    def __str__(self):
        return self.fullname

    # save button
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super(Author, self).save(*args, **kwargs)

    # return number of posts
    @property
    def num_posts(self):
        return Post.objects.filter(user=self).count()

    # return user group
    @property
    def user_name(self):
        return self.user

    #return user group
    @property
    def user_group(self):
        return (self.user).groups.all()[0].name

    #get user profile id
    @property
    def user_profile(self):
        return self.user.profile.id


#create sub forums
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    description = models.TextField(default="description")
    category_image = models.ImageField(
        null=True, blank=True, upload_to='flags/', default= "flags/flag-default.png")

#Meta is basically the inner class of your model class.
    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.title

    # save button
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

#acces to each category
    def get_url(self):
        return reverse("posts", kwargs={ #imported from django.shortcuts
            "slug": self.slug
        })

#get number of posts
    @property
    def num_posts(self):
        return Post.objects.filter(categories=self).count()

#get last post
    @property
    def last_post(self):
        return Post.objects.filter(categories=self).latest("date")



class Comment(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:100]


class Post(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE) #frame key of the author
    content = HTMLField()
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager() #imported from taggit.managers
    comments = models.ManyToManyField(Comment, blank=True)
    closed = models.BooleanField(default=False)

#save button
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

#acces to each post
    def get_url(self):
        return reverse("detail", kwargs={
            "slug":self.slug
        })

    @property
    def num_comments(self):
        return self.comments.count()

    @property
    def last_reply(self):
        return self.comments.latest("date")
