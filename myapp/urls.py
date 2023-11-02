from django.urls import path
from .views import CreateViewUser,Index,Congratulations

urlpatterns = [
    path('register/', CreateViewUser.as_view(), name='register'),
    path('', Index.as_view(), name='home'),
    path('congrats/', Congratulations.as_view(), name='congrats'),
]