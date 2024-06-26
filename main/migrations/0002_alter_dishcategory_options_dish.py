# Generated by Django 5.0.4 on 2024-05-01 15:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dishcategory',
            options={'ordering': ['sort'], 'verbose_name': 'Категорія страв', 'verbose_name_plural': 'Категорії страв'},
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('ingredients', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_visible', models.BooleanField(default=True)),
                ('sort', models.PositiveSmallIntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='dishes/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dishcategory')),
            ],
            options={
                'verbose_name': 'Страва',
                'verbose_name_plural': 'Страви',
                'ordering': ['sort'],
            },
        ),
    ]
