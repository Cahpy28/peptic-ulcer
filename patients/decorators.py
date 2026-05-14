from functools import wraps

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def verified_login_required(view_func):
    @login_required
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_active:
            messages.error(request, "Please verify your email before accessing your patient dashboard.")
            return redirect("login")
        return view_func(request, *args, **kwargs)

    return wrapper
