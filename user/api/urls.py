from django.urls import include, path
from user.api.views import registration_view

app_name = 'user'

urlpatterns = [
    path('register/',registration_view, name='register'),
]