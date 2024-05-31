from django.http import HttpResponseRedirect
from django.urls import reverse

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            # Redirect to the login page if the user is not authenticated
            login_url = reverse('admin:login')
            if request.path != login_url:
                return HttpResponseRedirect(login_url)

        # Continue processing the request
        response = self.get_response(request)
        return response
