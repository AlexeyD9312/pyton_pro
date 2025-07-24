from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password = None, **extra_fields):
        if not email:
            raise ValueError('Enter Email')
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True) 
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser shoud have staff status")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser shoud have superuser status")
        
        return self.create_user(email, password, **extra_fields) 


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique = True)
    full_name = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 20, blank = True)
    city = models.CharField(max_length = 200, blank = True)
    role = models.CharField(max_length = 20, choices = [('buyer', 'Покупатель'),('agent','Агент')], default = 'buyer')
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    date_joined = models.DateTimeField(auto_now_add = True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


    def __str__(self):
        return self.email


