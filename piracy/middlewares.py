from django.utils.deprecation import MiddlewareMixin


class DummyAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.user = {
            "name": request.COOKIES.get("piracy_user"),
        }
        response = self.get_response(request)
        return response
