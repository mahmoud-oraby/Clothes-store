from rest_framework import generics,permissions,authentication
from .models import User
from .serializers import RegisterSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        """
        Override the base method to add custom claims to the token.
        """
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    """
    Override the default TokenObtainPairView to use the custom serializer.
    """
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.ListCreateAPIView):
    """
    API view for user registration.
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes= []
