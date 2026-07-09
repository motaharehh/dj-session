from django.db import models

# Create your models here.

class Session(models.Model):
    session_key = models.CharField(
        max_length=64,
        unique=True,
    )

    session_data = models.TextField(
        default="",
    )

    def __str__(self):
        return self.session_key