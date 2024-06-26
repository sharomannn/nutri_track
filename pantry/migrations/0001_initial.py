# Generated by Django 5.0.6 on 2024-06-20 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PantryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
                ('quantity', models.FloatField(verbose_name='количество')),
                ('unit', models.CharField(max_length=50, verbose_name='единица измерения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания записи')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения данных')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ('name',),
            },
        ),
    ]
