from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
import datetime


class Messages(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User)
    message = models.TextField()
    date_time = models.DateTimeField(default=datetime.datetime.now())

    def __repr__(self):
        return '{0}: {1}'.format(self.user, self.message)


class MessagesAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'date_time')
