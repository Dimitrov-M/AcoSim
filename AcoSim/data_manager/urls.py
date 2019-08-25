from django.urls import path
from data_manager.views import CreateBucket, CheckBucket

urlpatterns = [
    path('create_bucket/', CreateBucket.as_view()),
    path('check_bucket/', CheckBucket.as_view()),
]