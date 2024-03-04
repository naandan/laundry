from functools import wraps
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.account_type == role:
                return view_func(request, *args, **kwargs)
            else:
                if request.user.is_authenticated :
                    if request.user.account_type == 'admin':
                        return redirect('/administrator')
                    elif request.user.account_type == 'petugas':
                        return redirect('/petugas')
                    elif request.user.account_type == 'pimpinan':
                        return redirect('/pimpinan')
                        
                return HttpResponseForbidden("Anda tidak memiliki izin untuk mengakses halaman ini.")
        return wrapper
    return decorator

def guest(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            if request.user.is_authenticated :
                if request.user.account_type == 'admin':
                    return redirect('/administrator')
                elif request.user.account_type == 'petugas':
                    return redirect('/petugas')
                elif request.user.account_type == 'pimpinan':
                    return redirect('/pimpinan')

            return HttpResponseForbidden("Anda tidak memiliki izin untuk mengakses halaman ini.")
    return wrapper