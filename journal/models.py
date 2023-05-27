from django.db import models
from django.forms import CharField
# Create your models here.


# import user model to use it as foreign key.

from django.contrib.auth.models import User


class Notes(models.Model):
    title = models.CharField(max_length=85)

    content = models.CharField(max_length=300)

    date_posted = models.DateTimeField(auto_now_add=True)

    # this is where we reference the user as a foreign key

    user = models.ForeignKey(
        User, max_length=10, on_delete=models.CASCADE, null=True)
