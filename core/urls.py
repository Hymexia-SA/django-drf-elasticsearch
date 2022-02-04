from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('search/', include('search.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('oauth2/', include('django_auth_adfs.urls')),
]
