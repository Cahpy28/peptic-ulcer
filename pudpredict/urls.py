from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.urls import include, path
from django.views.generic.base import RedirectView

from patients.forms import VerifiedAuthenticationForm


urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url="/static/assets/pudpredict-favicon.svg?v=8", permanent=True)),
    path("accounts/login/", LoginView.as_view(authentication_form=VerifiedAuthenticationForm, template_name="registration/login.html"), name="login"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("patients.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

