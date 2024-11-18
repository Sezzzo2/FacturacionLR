from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('usuario', '')
            password = request.POST.get('contrasena', '')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos', 'usuario': username})
        return render(request, 'login.html', {'usuario': ''})
    else:
        return redirect('inicio')

@login_required
def inicio_view(request):
    return render(request, 'inicio.html')
    
def logout_view(request):
    logout(request)
    return redirect('empleado_login')

