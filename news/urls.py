from .views import home_page,contact_page
from django.urls import path




urlpatterns=[
    path('',home_page,name='home'),
    path('contact/',contact_page,name='kontakt'),
]

