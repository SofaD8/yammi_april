# Generated by Django 5.0.4 on 2024-05-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_dishcategory_options_dish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chefs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('sort', models.PositiveSmallIntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='chefs/')),
            ],
            options={
                'verbose_name': 'Кухар',
                'verbose_name_plural': 'Кухарі',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='EventsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sort', models.PositiveSmallIntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='events/')),
            ],
            options={
                'verbose_name': 'Захід',
                'verbose_name_plural': 'Заходи',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort', models.PositiveSmallIntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
            ],
            options={
                'verbose_name': 'Світлина',
                'verbose_name_plural': 'Світлини',
                'ordering': ['sort'],
            },
        ),
    ]
