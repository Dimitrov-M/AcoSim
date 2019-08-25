import requests

from django.http import HttpResponse
from django.views import View


class GetAuthToken(View):
    def get(self, request):
        req = requests.post(
        	'https://developer.api.autodesk.com/authentication/v1/authenticate',
        	headers = {
        		'Content-Type': 'application/x-www-form-urlencoded',
        	},
        	data = {
        		'client_id': 'SnH41L3v1OqdeDZGIIZAf7oEz0WXqVCz',
        		'client_secret': 'AjAqZKwaPLVD8C9e',
        		'grant_type': 'client_credentials',
        		'scope': 'data:read',
        	}
        )
        return HttpResponse(req.text)
