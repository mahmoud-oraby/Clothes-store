from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email=None, password=None):
        """
        Create and save a new user with the given details.
        """
        if email is None:
            raise TypeError('Users Should have a email')
        
        user = self.model(email=self.normalize_email(email),first_name=first_name,last_name=last_name)
        user.set_password(password)
        user.save()
        return user
    
    
    def create_superuser(self, email, first_name, last_name, password=None,**kwargs):
        """
        Create and save a new superuser with the given details.
        """
        if password is None:
            raise TypeError('Password Should not be none')

        user = self.create_user(first_name,last_name ,email , password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=18)
    last_name = models.CharField(max_length=18)
    email = models.EmailField(max_length=255,unique=True,db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = UserManager()

    def __str__(self):
        """
        Return a string representation of the user (email address).
        """
        return self.email
    
    def tokens(self):
        """
        Generate and return JWT tokens for the user.
        """
        refresh = RefreshToken.for_user(self)

        return {
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }

    