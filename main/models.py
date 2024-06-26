from django.db import models
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField


# Create your models here.
class DishCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()


    def __iter__(self):
        for dish in self.dishes.filter(is_visible=True):
            yield dish

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія страв'
        verbose_name_plural = 'Категорії страв'
        ordering = ['sort']


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ingredients = models.TextField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE, related_name='dishes')
    sort = models.PositiveSmallIntegerField()

    photo = models.ImageField(upload_to='dishes/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страва'
        verbose_name_plural = 'Страви'
        ordering = ['sort']


class EventsCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_visible = models.BooleanField(default=True)
    description = RichTextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sort = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to='events/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Захід'
        verbose_name_plural = 'Заходи'
        ordering = ['sort']


class Chefs(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = RichTextField(blank=True, null=True)
    sort = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to='chefs/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кухар'
        verbose_name_plural = 'Кухарі'
        ordering = ['sort']


class Gallery(models.Model):
    sort = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to='gallery/', blank=True, null=True)

    def __int__(self):
        return self.sort

    class Meta:
        verbose_name = 'Світлина'
        verbose_name_plural = 'Світлини'
        ordering = ['sort']


class Reservation(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?(380)?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+9999999999'. Up to 15 digits allowed.")

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, validators=[phone_regex])
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    count = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)

    is_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.name} - {self.date} {self.time}'

    class Meta:
        verbose_name = 'Бронювання'
        verbose_name_plural = 'Бронювання'
        ordering = ('-date_created',)