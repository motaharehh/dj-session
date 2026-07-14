from django.db import models
import secrets

# Create your models here.

class Session(models.Model):
    session_key = models.CharField(
        max_length=64,
        unique=True,
    )

    session_data = models.TextField(
        default="",
    )

    @classmethod
    def create(cls):
        session = cls.objects.create(
            session_key=secrets.token_hex(32)
    )
        return session 

    def __str__(self):
        return self.session_key