from django.utils.deprecation import MiddlewareMixin


class DummyAuthMiddleware(MiddlewareMixin):
    roles = {
        "Alice": "admin",
        "Bob": "user",
    }

    def process_request(self, request):
        username = request.COOKIES.get("piracy_user")
        request.user = {
            "username": username,
            "role": self.roles.get(username),
        }
        response = self.get_response(request)
        return response
