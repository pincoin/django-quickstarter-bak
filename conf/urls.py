from django.conf.urls import (
    url, include
)
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
