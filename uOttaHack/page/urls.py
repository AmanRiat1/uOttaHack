from django.urls import include, path

from .views import index, about, test, question_create_view

urlpatterns = [
    path('', index, name='index'),
    path('/about', about, name='index'),
    path('test/', test),
    path('create/', question_create_view)
]