from django.urls import path
from . import views

app_name = 'myapp1'
urlpatterns = [
 path('', views.index, name='index'),
 path('about/', views.about, name='about'),
 path('about/<int:year>/<int:month>', views.about, name='about'),
 path('myapp/<int:type_no>', views.detail, name='myapp'),
 path('items/', views.items, name='items'),
 path('placeorder/', views.placeorder, name='placeorder'),
]