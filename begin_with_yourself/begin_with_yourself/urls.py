from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('news/', include('news.urls', namespace='news')),
    path('about/', include('about.urls', namespace='about')),
    path('auth/', include('users.urls', namespace='users'))
]
