from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/about', views.about, name='index'),
    path('test/', views.test),
    path('name/', views.name)

]