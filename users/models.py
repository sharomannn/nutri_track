from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField('возраст', null=True, blank=True)
    weight = models.FloatField('вес', null=True, blank=True)
    height = models.FloatField('рост', null=True, blank=True)
    dietary_preferences = models.TextField('диетические предпочтения', null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='группы, к которым принадлежит этот пользователь. Пользователь получит все разрешения, предоставленные каждой из его групп.',
        verbose_name='группы',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='специфические разрешения для этого пользователя.',
        verbose_name='разрешения пользователя',
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
