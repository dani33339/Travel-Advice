
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', include("forum.urls")),
    path('', include("trips.urls")),
    path('tinymce/', include('tinymce.urls')),
    path('account/', include('register.urls')),

]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)# connect MEDIA_URL with MEDIA_ROOT in settings