from django.utils import timezone
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.translation import ugettext_lazy as _
import pdb

class GnUserManager(BaseUserManager):
    def _create_user(self, email, username, password, is_staff, is_admin, **extra_fields):
            if not username:
                raise ValueError('The given email must be set')

            user = self.model(
                username = username,
                email = self.normalize_email(email),
                is_staff = is_staff,
                is_active = True,
                is_admin = is_admin,
                last_login = timezone.now(),
                **extra_fields
            )

            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_user(self, username, password = None, **extra_fields):
        pbd.start_trace()
        return self._create_user(username, password, False, False, **extra_fields)

    def create_superuser(self, username, password = None, **extra_fields):
        return self._create_user(username, password, True, True, **extra_fields)


class GnUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=250, unique=True)
    first_name = models.CharField(max_length=250, blank=True)
    second_name = models.CharField(max_length=250, blank=True)
    third_name = models.CharField(max_length=250, blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_active   = models.BooleanField(default=True)
    is_admin    = models.BooleanField(default=False)
    is_staff    = models.BooleanField(default=False)
    # vk_id = models.

    objects = GnUserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        # The user is identified by their email address
        return '%s %s %s' % (self.first_name, self.second_name, self.third_name)

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin
