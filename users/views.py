from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from.models import Profile
from .forms import ProfileForm



def profiles(request): 
    """ main page of the all guides """
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def guideProfile(request,pk): 
    """ profile that travelare see """
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile': profile,'topSkills':topSkills,
                'otherSkills':otherSkills}
    return render(request,'users/guide-profile.html',context)

@login_required(login_url='login')
def userAccount(request): 
    """ account page of the guide """
    profile = request.user.profile
    Skills = profile.skill_set.all()
    trips = profile.trip_set.all()

    context = {'profile':profile, 'skills':Skills, 'trips':trips}
                
    return render(request,'users/account.html',context)


@login_required(login_url='login')
def editAccount(request): 
    """ edit the guide profile """
    profile = request.user.profile

    form = ProfileForm(instance=profile)# all fileds of profile


    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form':form}
    return render(request, 'users/profile_form.html',context)