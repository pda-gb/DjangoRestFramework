import uuid

from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4,
                          editable=False)
    STATUS_CHOICES = [
        (1, 'администратор'),
        (2, 'менеджер'),
        (3, 'пользователь'),
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=3)
    username = models.CharField(max_length=32, unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=32, unique=True, blank=False)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.username, self.status}"
