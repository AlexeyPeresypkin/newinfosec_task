from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class UserRole:
        USER = 'user'
        ADMIN = 'admin'
        choices = [
            (USER, 'user'),
            (ADMIN, 'admin'),
        ]

    role = models.CharField(
        max_length=25,
        choices=UserRole.choices,
        default=UserRole.USER,
    )


class Resource(models.Model):
    WINDOWS = 'WNS'
    UNIX = 'UNX'
    SQL = 'SQL'
    TYPE_OF_RESOURCE = [
        (WINDOWS, 'Windows'),
        (UNIX, 'Unix'),
        (SQL, 'SQL')
    ]
    ip = models.CharField(
        max_length=32,
        verbose_name='Ip адрес'
    )
    port = models.SmallIntegerField(
        verbose_name='Порт'
    )
    type_resource = models.CharField(
        max_length=3,
        choices=TYPE_OF_RESOURCE,
        verbose_name='Тип ресурса'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='recipes'
    )
    date_edit = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата и время редактирования'
    )

    def __str__(self):
        return f'{self.owner} {self.type_resource}'

    class Meta:
        ordering = ['-date_edit']
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурсы'
