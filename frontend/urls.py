from django.urls import path
from .views import carfax, carfax_results

urlpatterns = [
    path('carfax/', carfax, name='carfax'),
    path('carfax/results/', carfax_results, name='carfax_results'),
]