
from django.urls import path
from store import views

urlpatterns = [
    path('', views.IndexView, name='index'),
]
