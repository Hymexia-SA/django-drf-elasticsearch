from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('search/', include('search.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
]
