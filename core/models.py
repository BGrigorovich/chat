from django.db import models
from django.contrib.auth.models import User
import datetime


class Messages(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User)
    message = models.TextField()
    date_time = models.DateTimeField()

    def __str__(self):
        return self.message

    @classmethod
    def create(cls, user, message):
        new_message = cls(user=user, message=message, date_time=datetime.datetime.now())
        return new_message
