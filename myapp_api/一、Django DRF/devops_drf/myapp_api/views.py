from rest_framework import viewsets
from .serializers import UserSerializer
from myapp_api.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer