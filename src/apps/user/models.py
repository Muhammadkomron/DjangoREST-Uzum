from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import BaseModel
from apps.user.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    """
    Note:
        this table holds information about
        users and fetched based on the role
    """
    username = models.CharField(max_length=255, unique=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.',
        ),
    )
    is_superuser = models.BooleanField(_('superuser status'), default=False)
    is_blocked = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        ordering = ('-id',)
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return f'{self.username}'
