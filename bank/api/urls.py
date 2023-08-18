from django.urls import path, include

urlpatterns = [
    path('user/', include("bank.user.urls")),
]
