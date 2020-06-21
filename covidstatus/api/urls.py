from django.urls import path

from covidstatus.api.views import get_latest_status,get_health_facilities,get_testing_health_facilities,get_latest_news

app_name = 'covidstatus'

urlpatterns= [
    path('status/', get_latest_status, name='covid-status'),
    path('health-facilities/', get_health_facilities, name='health-facilities'),
    path('health-facilities/testing/', get_testing_health_facilities, name='testing-health-facilities'),
    path('news/', get_latest_news, name='covid-news'),
]