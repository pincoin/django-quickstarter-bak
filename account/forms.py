import logging

from django import forms
from django.contrib.auth.forms import (
    ReadOnlyPasswordHashField
)
from django.utils.translation import ugettext_lazy as _
from registration.forms import (
    RegistrationFormUniqueEmail, RegistrationFormTermsOfService
)

from .models import (
    User, UserManager
)


class UserCreationForm(forms.ModelForm):
    logger = logging.getLogger(__name__)

    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    email = forms.EmailField(
        label=_('Email'),
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Email address'),
                'required': 'True',
            }
        )
    )
    last_name = forms.CharField(
        label=_('Last name'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Last name'),
                'required': 'True',
            }
        )
    )
    first_name = forms.CharField(
        label=_('First name'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('First name'),
                'required': 'True',
            }
        )
    )
    username = forms.CharField(
        label=_('Username'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Username'),
                'required': 'True',
            }
        )
    )
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password'),
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password confirmation'),
                'required': 'True',
            }
        )
    )

    class Meta:
        model = User
        fields = ('email', 'last_name', 'first_name', 'username')

    def save(self, commit=True):
        self.logger.debug('UserCreationForm.save()')

        user = super(UserCreationForm, self).save(commit=False)

        user.email = UserManager.normalize_email(self.cleaned_data['email'])
        # Save the provided password in hashed format
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True

        if commit:
            user.save()

        return user

    def clean_password2(self):
        self.logger.debug('UserCreationForm.clean_password2()')

        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords don't match"))

        return password2


class UserChangeForm(forms.ModelForm):
    logger = logging.getLogger(__name__)

    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField(
        label=_('Password')
    )

    class Meta:
        model = User
        fields = ('email', 'password', 'last_name', 'first_name', 'is_active', 'is_superuser', 'is_staff')

    def clean_password(self):
        self.logger.debug('UserChangeForm.clean_password()')

        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class WebUserCreationForm(RegistrationFormUniqueEmail, RegistrationFormTermsOfService):
    #  A form for creating new users on web interface.

    class Meta:
        # Custom User model must be designated here!
        model = User
        # Input fields must be listed here!
        fields = ('email', 'last_name', 'first_name', 'username')
