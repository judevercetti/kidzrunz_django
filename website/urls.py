from django.urls import include, path

from website import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/<slug:slug>', views.aboutus, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('activities', views.activities, name='activities'),
    path('activities/<slug:slug>', views.activities, name='activities'),
    path('leadership', views.leadership, name='leadership'),
    path('mission', views.mission, name='mission'),
    path('services', views.services, name='services'),
    path('consultation', views.consultation, name='consultation'),
    path('contact', views.contactus, name='contact'),
    path('faqs', views.faqs, name='faqs'),
    # path('terms-and-conditions', views.termsandconditions, name='terms-and-conditions'),
    path('safeguarding-and-enhanced-dbs', views.safeguardingandenhanceddbs, name='safeguarding-and-enhanced-dbs'),
    path('who-cams-are', views.who_cams_are, name='who-cams-are'),
    path('mindfulness-approach', views.mindfuless_approach, name='mindfulness-approach'),
    path('cams', views.cams, name='cams'),

    path('blog', views.blog, name='blog'),
    path('blog/terms-and-conditions', views.termsandconditions, name='terms-and-conditions'),
    path('blog/privacy-policy', views.privacy_policy, name='privacy-policy'),
    path('blog/<slug:slug>', views.blog_details, name='blog-details'),
]
