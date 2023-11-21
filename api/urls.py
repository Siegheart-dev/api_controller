from django.urls import path
from .views import Func

urlpatterns = [
    path('ipa', Func.as_view()),
]