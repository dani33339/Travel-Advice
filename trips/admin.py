from django.contrib import admin

# Register your models here.
from .models import Trip,Review,Tag

#כדי שנולך לראות את הנתונים בבסיס נתונים בפאנל של האדמין
admin.site.register(Trip)
admin.site.register(Review)
admin.site.register(Tag)