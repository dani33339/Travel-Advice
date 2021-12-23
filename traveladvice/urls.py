
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from contact.views import  contact_view,aboutus


urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', include("forum.urls")),
    path('', include("trips.urls")),
    path('users/', include("users.urls")),
    path('tinymce/', include('tinymce.urls')),
    path('account/', include('register.urls')),
    path('contact/',contact_view,name='contact'),
    path('aboutus/',aboutus,name='aboutus'),

]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)# connect MEDIA_URL with MEDIA_ROOT in settings
urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)# connect MEDIA_URL with MEDIA_ROOT in settings