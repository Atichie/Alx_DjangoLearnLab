from django.db import models

# Create your models here
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()

    class Meta:
        permissions = [
                ("can_view", "Can view books"),
                ("can_create", "Can create books"),
                ("can_edit", "Can edit books"),
                ("can_delete", "Can delete books"),
        ]

from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, date_of_birth=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, dte_of_birth, password, **extra_fields)


from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photo/', null=True, blank=True)
    objects = CustomUserManager()


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        permissions = [
                ("can_view", "Can view articles"),
                ("can_create", "Can create articles"),
                ("can_edit", "Can edit articles"),
                ("can_delete", "Can delete articles"),
        ]

