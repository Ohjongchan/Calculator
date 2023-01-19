from django.urls import path
from saving.views import hello_world

app_name = "saving"

urlpatterns = [
    path('hello world/', hello_world, name='hello_world')
]