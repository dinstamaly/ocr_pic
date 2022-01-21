from django.urls import path
from .views import *


urlpatterns = [
   path('', HomeView.as_view()),
   path('process_image', process_image, name='process_image') # New line
]