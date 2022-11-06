from time import sleep


class WaitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.count_request = 0
        self.when_wait = 3

    def __call__(self, request):
        self.count_request += 1

        if self.count_request % self.when_wait == 0:
            sleep(5)

        return self.get_response(request)