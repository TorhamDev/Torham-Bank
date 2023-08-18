from django.urls import path
from bank.user.views import AccountRegister

urlpatterns = [
    path('register/', AccountRegister.as_view()),
]
