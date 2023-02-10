from django.urls import path
from . import views

app_name = 'myapp1'
urlpatterns = [
 path('', views.index, name='index'),
]