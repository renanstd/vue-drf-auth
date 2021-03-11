from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from core import models


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Todo
        fields = ['id', 'name', 'content', 'date', 'done']


class CustomTokenOptainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Adiciona informações no retorno do token
        token['username'] = user.username

        return token
