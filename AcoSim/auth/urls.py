from django.urls import path
from auth.views import GetAuthToken

urlpatterns = [
    path('get_token/', GetAuthToken.as_view()),
]