from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    """
        Maintain user and its attributes
    """
    @property
    def group_name(self):
        """
        Returns a group name based on the user's id to be used by Django Channels.
        Example usage:
        user = User.objects.get(pk=1)
        group_name = user.group_name
        """
        return "user_%s" % self.id