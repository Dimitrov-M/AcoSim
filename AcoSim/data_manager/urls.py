from django.urls import path
from data_manager.views import CreateBucket, CheckBucket, UploadToBucket

urlpatterns = [
    path('create_bucket/', CreateBucket.as_view()),
    path('check_bucket/', CheckBucket.as_view()),
    path('upload_to_bucket/', UploadToBucket.as_view()),
]