from django.urls import include, path

from website import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.aboutus, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('activities', views.activities, name='activities'),
    path('leadership', views.leadership, name='leadership'),
    path('mission', views.mission, name='mission'),
    path('services', views.services, name='services'),
    path('consultation', views.consultation, name='consultation'),
    path('contact', views.contactus, name='contact'),
    path('terms-and-conditions', views.termsandconditions, name='terms-and-conditions'),
    path('safeguarding-and-enhanced-dbs', views.safeguardingandenhanceddbs, name='safeguarding-and-enhanced-dbs'),
]
