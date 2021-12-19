from enum import unique
from django.db import models
import uuid
from users.models import Profile
# Create your models here.


class Trip(models.Model): 
    owner = models.ForeignKey(
        Profile,null=True, blank= True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank = True)
    featured_image = models.ImageField(null = True, blank = True, default= "default.jpg")# upload image from the trip, and by the default its gray image 
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True) #one trip has many tag and vice versa
    vote_total = models.IntegerField(default=0, null=True, blank=True)# all the vote that the trips has
    vote_ration = models.IntegerField(default=0, null=True, blank=True)# the ration betwen negative and positive
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    
    def __str__(self): 
        return self.title
    class Meta: 
        ordering = ['-vote_ration','-vote_total', 'title']
        
    @property   
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset
    
    def getVoteCount(self): 
        review = self.review_set.all()
        upVotes = review.filter(value='up').count()
        totalVotes = review.count()

        ration = (upVotes/totalVotes)*100
        self.vote_total = totalVotes
        self.vote_ration = ration
        self.save()


class Review(models.Model): 
    VOTE_TYPE = ( 
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices= VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    # its make possible to lave only one review
    class Meta: 
        unique_together = [['owner', 'trip']]

    def __str__(self): 
        return self.value

class Tag(models.Model): 
    name = models.CharField(max_length=200) 
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self): 
        return self.name