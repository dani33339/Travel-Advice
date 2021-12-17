from django.shortcuts import render
from.models import Profile



def profiles(request): 
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def guideProfile(request,pk): 
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile': profile,'topSkills':topSkills,
                'otherSkills':otherSkills}
    return render(request,'users/guide-profile.html',context)