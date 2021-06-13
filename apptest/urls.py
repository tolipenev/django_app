from django.urls import path
from . import views

  
app_name = 'apptest'
urlpatterns = [
    path('', views.form_view, name='index'),
    path('', views.Engagement, name='index'),
    path('', views.Entity, name='index'),
]