import uuid

from django.apps import apps
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        # if not username:
        #     raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username=None, email=None, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text=_(
            "The unique identifier of the user. Mandatory, unless a new instance to create is given."
        ),
    )

    email = models.EmailField(
        verbose_name=_("Email"),
        unique=True,
        db_index=True,
        help_text=_("The primary email address of the user"),
    )

    NULL_AND_BLANK = {"null": True, "blank": True}


    first_name = models.CharField(
        verbose_name=_("First Name"),
        max_length=125,
        **NULL_AND_BLANK,
        help_text=_(
            "First name of the user"
        ),
    )

    last_name = models.CharField(
        verbose_name=_("Last Name"),
        max_length=125,
        **NULL_AND_BLANK,
        help_text=_(
            "Last name of the user"
        ),
    )
    
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        null=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now, blank=True)

    @property
    def fullname(self):
        name = (self.first_name or '') + ' ' + (self.last_name or '')
        name = name.strip()
        if len(name) == 0:
            name = 'Anonymous'
        return name
