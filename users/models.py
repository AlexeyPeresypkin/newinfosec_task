from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


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
        choices=TYPE_OF_RESOURCE
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
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурсы'
