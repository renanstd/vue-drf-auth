from rest_framework import serializers
from core import models


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Todo
        fields = ['id', 'name', 'content', 'date', 'done']
