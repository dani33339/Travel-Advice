from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from.models import Profile
from .forms import ProfileForm,SkillForm,GuideForm, ReviewForm
from django.contrib import messages
from .utils import searchProfiles


def profiles(request): 
    """ main page of the all guides """
    profiles, search_query = searchProfiles(request)
    #profiles = Profile.objects.all()
    context = {'profiles': profiles, 'search_query': search_query}
    return render(request, 'users/profiles.html', context)

def guideProfile(request,pk): 
    """ profile that travelare see """
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit = False)
        review.vote = profile
        review.owner = request.user.profile
        review.save()
        profile.getVoteCount()
        messages.success(request, 'Succefully Vote.')
        return redirect('guide-profile',pk=profile.id)
    else:
        messages.error(request, 'Already Vote')

    context = {'profile': profile,'topSkills':topSkills,
                'otherSkills':otherSkills, 'form':form}
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
    if request.user.groups.filter(name="guide"):
        form = GuideForm(instance=profile)
    else:
        form = ProfileForm(instance=profile)# all fileds of profile


    if request.method == 'POST':
        if request.user.groups.filter(name="guide"):
            form = GuideForm(request.POST, request.FILES, instance=profile)
        else:
            form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form':form}
    return render(request, 'users/profile_form.html',context)

@login_required(login_url='login')
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill was added successfully!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill was updated successfully!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill was deleted successfully!')
        return redirect('account')

    context = {'object': skill}
    return render(request, 'delete_template.html', context)

