from django.http import HttpResponse
from django.views import View


class GetAuthToken(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('token received')