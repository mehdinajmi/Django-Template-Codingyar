from django.urls import path
from .views import home_page,about_us,contact_us

urlpatterns = [
    path('', home_page,name='homepage'),
    path('about/', about_us,name='aboutus'),
    path('contact/', contact_us,name='contactus'),
]