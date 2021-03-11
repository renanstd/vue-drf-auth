from rest_framework import viewsets
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from core import models
from core.api import serializers


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to add/edit/remove todos.
    """
    serializer_class = serializers.TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the todos
        for the currently authenticated user.
        """
        user = self.request.user
        return models.Todo.objects.filter(user=user)


class CustomTokenOptainPairViewSet(TokenObtainPairView):
    serializer_class = serializers.CustomTokenOptainPairSerializer
