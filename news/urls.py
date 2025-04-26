from .views import home_page,contact_page,detail_page,mahalliy_news_page
from django.urls import path




urlpatterns=[
    path('',home_page,name='home'),
    path('contact/',contact_page,name='kontakt'),
    path('mahalliy/',mahalliy_news_page,name='local_new'),
    path('detail/<slug:slug>/',detail_page,name='new_detail'),
]

