from django.contrib import admin

# Register your models here.
from .models import Profile, Skill, review

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(review)