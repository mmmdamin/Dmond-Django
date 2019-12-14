from datetime import datetime

from django.utils.deprecation import MiddlewareMixin


class BenchmarkMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request._request_time = datetime.now()

    def process_response(self, request, response):
        response_time = request._request_time - datetime.now()
        print(response_time)
        return response
