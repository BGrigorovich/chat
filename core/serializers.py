from rest_framework import serializers
from .models import Messages, User


class MessagesSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Messages
        fields = ('user', 'message', 'date_time')
