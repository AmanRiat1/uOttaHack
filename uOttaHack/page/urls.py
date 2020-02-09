from django.urls import include, path

<<<<<<< HEAD
from .views import index, about, test, question_create_view
=======
urlpatterns = [
    path('', views.index, name='index'),
    path('/about', views.about, name='index'),
    path('test/', views.test),
    path('name/', views.name)
>>>>>>> 4751f810dcbaea1ab594834a78889f0f251ab8bd

urlpatterns = [
    path('', index, name='index'),
    path('/about', about, name='index'),
    path('test/', test),
    path('create/', question_create_view)
]