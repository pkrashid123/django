from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name = 'home'),
    path('Services', views.services, name = 'services'),
    path('Teacher', views.teacher, name = 'teachers'),
    path('About', views.about, name = 'about'),
    path('Pricing', views.pricing, name = 'pricing'),
    path('Contact', views.contact, name = 'contact'),
]
