from django.shortcuts import redirect
from django.urls import reverse


class RedirectIfAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.path in [reverse('accounts:login'), reverse('accounts:register')]:
                return redirect('learning_logs:index')
        response = self.get_response(request)
        return response


class RedirectIfNotAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            if request.path == reverse('accounts:logout'):
                return redirect('learning_logs:index')
        response = self.get_response(request)
        return response
