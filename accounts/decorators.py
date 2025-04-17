from django.shortcuts import redirect

def status_user(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_active:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper