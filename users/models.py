from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from PIL import Image


class MyUserManager(BaseUserManager):

    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,  **other_fields)
        user.set_password(password)
        other_fields.setdefault('is_active', True)
        user.save()
        return user

    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(_("Super user must be assigned to is_staff=True."))

        if other_fields.get('is_superuser') is not True:
            raise ValueError(_("Super user must be assigned to is_superuser=True."))

        return self.create_user(email, username, password, **other_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]

    username = models.CharField(
        _("username"),
        max_length=50,
        unique=True,
        help_text=_("Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)
    email = models.EmailField(_('email'), unique=True)
    phone_number = models.BigIntegerField(_('phone number'), unique=True, blank=True, null=True,
                                          validators=[
                                              validators.RegexValidator(r'^989[0-3,9]\d{8}$',
                                                                        _("Enter a valid mobile number."),
                                                                        'invalid')])
    is_staff = models.BooleanField(_('staff'), default=False)
    is_active = models.BooleanField(_('active'), default=False)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True)
    profile_picture = models.ImageField(_('profile picture'), default='default.jpg', upload_to='profile_pictures')
    biography = models.TextField(_('biography'), blank=True)
    gender = models.CharField(_('gender'), choices=GENDER_CHOICES, blank=True, max_length=10)
    birthday = models.DateField(_('birthday'), blank=True, null=True)

    objects = MyUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super(MyUser, self).save(*args, **kwargs)

        img = Image.open(self.profile_picture.path)

        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)

    def activate_account(self):
        self.is_active = True

    class Meta:
        db_table = 'MyUser'
        verbose_name = _('user')
        verbose_name_plural = _('users')
