from django.shortcuts import render
from.models import Profile



def profiles(request): 
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def guideProfile(request): 
    return render(request,'uresr/guide-profile.html')