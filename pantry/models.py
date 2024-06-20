from django.db import models
from django.contrib.auth import get_user_model

class PantryItem(models.Model):
    user = models.ForeignKey(
        'users.CustomUser',
        verbose_name='пользователь',
        on_delete=models.CASCADE,
        related_name='pantry_items'
    )
    name = models.CharField('название', max_length=255)
    quantity = models.FloatField('количество')
    unit = models.CharField('единица измерения', max_length=50)

    created_at = models.DateTimeField('дата создания записи', auto_now_add=True)
    updated_at = models.DateTimeField('дата последнего изменения данных', auto_now=True)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)

    def __str__(self) -> str:
        return f"{self.name} ({self.quantity} {self.unit})"