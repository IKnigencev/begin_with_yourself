from django.contrib import admin
from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', views.map, name='map'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('crate_idea/', views.create_idea, name='create_idea'),
    path('idead_edit/', views.idea_edit, name='idea_edit'),
    path('idea_detail/<int:idea_id>', views.idea_detail, name='idea_detail'),
    path('', views.main, name='index')
]
