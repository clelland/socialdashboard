from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class SocialUserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=email, is_staff=True, is_superuser=True, **kwargs)
        user.set_password(password)
        user.save()
        return user


class SocialUser(AbstractBaseUser):
    # Use a sufficiently long email field
    email = models.EmailField(verbose_name='email address', max_length=254, unique=True)

    twitter_screenname = models.CharField(max_length=20, null=True, blank=True)
    facebook_user_id = models.BigIntegerField(null=True, blank=True)
    google_plus_userid = models.CharField(max_length=50, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = SocialUserManager()

    def get_short_name(self):
        return self.twitter_screenname or self.email

    def get_full_name(self):
        if self.twitter_screenname:
            return "{0} ({1})".format(self.twitter_screenname, self.email)
        else:
            return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __unicode__(self):
       return self.get_full_name()

    def __str__(self):
        return self.__unicode__()
