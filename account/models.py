"""
import os
from hashlib import sha1, md5
"""

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, username, last_name, first_name, password=None):
        """
        Creates and saves a User with the given email, username,
        password and other information
        """
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            last_name=last_name,
            first_name=first_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, last_name, first_name, password):
        """
        Creates and saves a superuser with the given email, username and
        password and other information
        """
        user = self.create_user(
            email=email,
            password=password,
            username=username,
            last_name=last_name,
            first_name=first_name,
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('Email address'),
        help_text=_('Enter your correct email address.'),
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        verbose_name=_('Username'),
        help_text=_('Enter your username to display at the website'),
        max_length=150,
        unique=True
    )
    first_name = models.CharField(
        verbose_name=_('First name'),
        help_text=_('Enter your first name.'),
        max_length=30,
        blank=True
    )
    last_name = models.CharField(
        verbose_name=_('Last name'),
        help_text=_('Enter your last name.'),
        max_length=30,
        blank=True
    )
    is_staff = models.BooleanField(
        verbose_name=_('Staff status'),
        help_text=_('Designates whether the user can log into this admin site.'),
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name=_('Is active'),
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
        default=True,
    )
    date_joined = models.DateTimeField(
        verbose_name=_('Date joined'),
        default=timezone.now
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'last_name', 'first_name', ]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined',)

    def __str__(self):
        return self.username

    def get_full_name(self):
        """
        Returns the last name plus the first_name, without a space in between.
        """
        full_name = '%s %s' % (self.last_name, self.first_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    get_full_name.short_description = _('Full name')
