from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
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
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("patients.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

