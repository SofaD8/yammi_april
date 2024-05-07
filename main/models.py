from django.db import models


# Create your models here.
class DishCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)
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
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE)
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
    description = models.TextField(blank=True, null=True)
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
    description = models.TextField(blank=True, null=True)
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
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    class Meta:
        verbose_name = 'Світлина'
        verbose_name_plural = 'Світлини'
        ordering = ['sort']