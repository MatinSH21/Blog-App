from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User


class MyUser(AbstractBaseUser, PermissionsMixin):

    firstname
