from django.urls import path
from .views import home, patient_list

urlpatterns = [
    path('', home, name='home'),
    path('patients/', patient_list, name='patient_list'),
]