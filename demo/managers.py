from django.contrib.auth.models import BaseUserManager


class Usermanager(BaseUserManager):

    def create_user(self, email, password, name=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")
        
        user = self.model(
            email = self.normalize_email(email=email),
            name = name,
            **extra_fields
        )

        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password, name=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, name, **extra_fields)
