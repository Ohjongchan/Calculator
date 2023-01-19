from django.urls import path
from saving.views import cal

app_name = "saving"

urlpatterns = [
    path('cal/', cal, name='calculator')
]