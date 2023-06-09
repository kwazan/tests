from .models import BlockedIP
from django.core.exceptions import PermissionDenied

class BlockedIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if BlockedIP.objects.filter(ip_address=request.META['REMOTE_ADDR']).exists():
            raise PermissionDenied

        response = self.get_response(request)
        return response
