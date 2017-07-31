from django.conf import settings
from django.conf.urls import (
    url, include
)
from django.conf.urls.static import static
from django.contrib import admin
from registration.backends.hmac.views import RegistrationView

from account.forms import WebUserCreationForm

urlpatterns = [
    url(r'^admin/',
        admin.site.urls),

    url(r'^accounts/register/$',
        RegistrationView.as_view(
            form_class=WebUserCreationForm
        ), name='registration_register'),
    url(r'^accounts/',
        include('registration.backends.hmac.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
