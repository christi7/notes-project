from django.urls import path
from .views import index

app_name = 'games'

urlpatterns = [
    path('', index, name="hub")
]
