from django.db import models
from django.contrib.auth.models import User
import datetime


class Messages(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User)
    message = models.TextField()
    date_time = models.DateTimeField()

    @classmethod
    def create(cls, user, message):
        new_message = cls(user_id=user, message=message, date_time=datetime.datetime.now())
        return new_message
