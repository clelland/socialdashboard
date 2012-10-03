from django.contrib.admin import *
from socialuser.models import SocialUser

site.register(SocialUser, ModelAdmin)
