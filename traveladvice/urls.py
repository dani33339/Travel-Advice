
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', include("forum.urls")),
    path('', include("trips.urls")),
    path('tinymce/', include('tinymce.urls')),
    path('account/', include('register.urls')),

]
