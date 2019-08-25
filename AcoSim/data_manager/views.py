import requests

from django.http import HttpResponse
from django.views import View


class CreateBucket(View):
    def get(self, request):
        req = requests.post(
            'https://developer.api.autodesk.com/oss/v2/buckets',
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0.eyJjbGllbnRfaWQiOiJTbkg0MUwzdjFPcWRlRFpHSUlaQWY3b0V6MFdYcVZDeiIsImV4cCI6MTU2NjczNDQ1Mywic2NvcGUiOlsiYnVja2V0OmNyZWF0ZSIsImJ1Y2tldDpyZWFkIiwiZGF0YTp3cml0ZSJdLCJhdWQiOiJodHRwczovL2F1dG9kZXNrLmNvbS9hdWQvand0ZXhwNjAiLCJqdGkiOiJJR3luQWE0ZlozN0h3N0dSMjNrVjJUZDNXdmhXUWxrTG5LNzFWbko0MVpoNkhpZzRVOENyRElFSzBjV2RzQmoxIn0.wW4PZvX9i-u-fpW_abYRbbbMREJ02sXUfCacb81ccMo'
            },
            data = '{"bucketKey":"acosimbucket", "policyKey":"transient"}'
        )
        return HttpResponse(req.text)


class CheckBucket(View):
    def get(self, request):
        req = requests.get(
            'https://developer.api.autodesk.com/oss/v2/buckets/acosimbucket/details',
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0.eyJjbGllbnRfaWQiOiJTbkg0MUwzdjFPcWRlRFpHSUlaQWY3b0V6MFdYcVZDeiIsImV4cCI6MTU2NjczNDQ1Mywic2NvcGUiOlsiYnVja2V0OmNyZWF0ZSIsImJ1Y2tldDpyZWFkIiwiZGF0YTp3cml0ZSJdLCJhdWQiOiJodHRwczovL2F1dG9kZXNrLmNvbS9hdWQvand0ZXhwNjAiLCJqdGkiOiJJR3luQWE0ZlozN0h3N0dSMjNrVjJUZDNXdmhXUWxrTG5LNzFWbko0MVpoNkhpZzRVOENyRElFSzBjV2RzQmoxIn0.wW4PZvX9i-u-fpW_abYRbbbMREJ02sXUfCacb81ccMo',
            }
        )
        return HttpResponse(req.text)
