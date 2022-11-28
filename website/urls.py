from django.urls import include, path

from website import views

urlpatterns = [
    path('', views.index),
]
