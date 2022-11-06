from django.core.exceptions import PermissionDenied
import time


class ManyRequestsMiddleware:
    def __init__(self, get_response):
        self.ips = dict()
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")
        if ip in self.ips:
            self.ips[ip][0] += 1
            if time.time() - self.ips[ip][1] > 10 and self.ips[ip][0] > 3:
                self.ips[ip][0] = 1
                self.ips[ip][1] = time.time()
                raise PermissionDenied
        else:
            self.ips[ip] = [1, time.time()]
        response = self.get_response(request)
        return response
