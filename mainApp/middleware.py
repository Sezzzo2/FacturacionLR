from django.shortcuts import redirect
from django.conf import settings


class LoginRequiredMiddleware:
    """
    Middleware que requiere que el usuario esté autenticado para todas las vistas,
    excepto las definidas explícitamente como exentas.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        rutas_exentas = [
            '/login/',  
            '/logout/', 
        ]

        if not request.user.is_authenticated and request.path not in rutas_exentas:
            return redirect(settings.LOGIN_URL)  

        return self.get_response(request)

