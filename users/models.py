
from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.query import Prefetch
# Create your models here.
from django.db.models.signals import post_save

class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null= True)
    username =  models.CharField(max_length=200, blank=True, null=True)
    location =  models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank = True, null=True)
    bio = models.TextField(blank=True,null=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/', default= "profiles/user-default.png")
    guide_confirmation = models.ImageField(
        null=True, blank=True, upload_to='profiles/')
    admin_approved=models.BooleanField(default=False)
    vote_total = models.IntegerField(default=0, null=True, blank=True)  # all the vote that the trips has
    vote_ration = models.IntegerField(default=0, null=True, blank=True)  # the ration betwen negative and positive
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self): 
        return str(self.username)

    @property
    def reviewers(self):
        queryset = Review.objects.values_list('owner__id', flat=True)
        return queryset

    def reviewersList(self):
        queryset = Review.objects.filter(vote=self.id)
        return queryset

    def reviewersListId(self):
        queryset = Review.objects.filter(vote=self.id).values_list('owner__id', flat=True)
        return queryset

    def getVoteCount(self):
        review=Review.objects.filter(vote=self.id)
        upVotes = review.filter(value='up').count()
        totalVotes = review.count()

        ration = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ration = ration
        self.save()

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True,related_name = "owner")
    vote = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True,related_name = "vote")
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200,null=True, choices= VOTE_TYPE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    class Meta:
        unique_together = [['owner','vote']]


    def __str__(self):
        return self.value

class Skill(models.Model): 
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    
    def __str__(self): 
        return str(self.name)

def profileUpdated(sender, instance, created, **kwargs): 
    print('profile Saved!')
    print('Instance', instance)
    print('CREATED', created)



post_save.connect(profileUpdated, sender= Profile)