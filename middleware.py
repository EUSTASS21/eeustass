# middleware.py
from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    """Redirect to login if user is not authenticated."""
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            # Redirect to login page if not authenticated
            # Prevent redirect loop for the login page itself
            if request.path != reverse('login'):  # 'login' is the name you assigned in urls.py
                return redirect('login')  # Redirect to login URL

        response = self.get_response(request)
        return response
