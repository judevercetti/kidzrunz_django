from django.urls import include, path

from website import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.aboutus, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('activities', views.activities, name='activities'),
]
