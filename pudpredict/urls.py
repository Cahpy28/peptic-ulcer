from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (
    LoginView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.http import FileResponse
from django.urls import include, path
from pathlib import Path

from patients.forms import VerifiedAuthenticationForm


def favicon(request):
    icon_path = Path(settings.BASE_DIR) / "frontend" / "static" / "assets" / "pudpredict-favicon.svg"
    response = FileResponse(open(icon_path, "rb"), content_type="image/svg+xml")
    response["Cache-Control"] = "public, max-age=86400"
    return response


urlpatterns = [
    path("favicon.ico", favicon, name="favicon"),
    path("accounts/login/", LoginView.as_view(authentication_form=VerifiedAuthenticationForm, template_name="registration/login.html"), name="login"),
    path(
        "accounts/password-reset/",
        PasswordResetView.as_view(
            template_name="registration/password_reset_form.html",
            email_template_name="registration/password_reset_email.txt",
            html_email_template_name="registration/password_reset_email.html",
            subject_template_name="registration/password_reset_subject.txt",
            success_url="/accounts/password-reset/done/",
        ),
        name="password_reset",
    ),
    path(
        "accounts/password-reset/done/",
        PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "accounts/reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm.html",
            success_url="/accounts/reset/done/",
        ),
        name="password_reset_confirm",
    ),
    path(
        "accounts/reset/done/",
        PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),
        name="password_reset_complete",
    ),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("patients.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

