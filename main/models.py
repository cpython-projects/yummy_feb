from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True)
    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        db_table = 'main_categories'
        ordering = ('sort', 'name')
        verbose_name = 'Категорія страв'
        verbose_name_plural = 'Категорії'

    def __iter__(self):
        for dish in self.dishes.all():
            yield dish

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    desc = models.TextField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='dishes/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        db_table = 'main_dishes'
        ordering = ('sort', 'name')
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return self.name


class Contacts(models.Model):
    address = RichTextField()
    reservations = RichTextField()
    opening_hours = RichTextField()


class Reservations(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    number_guests = models.PositiveSmallIntegerField(default=1)
    message = models.TextField(max_length=255)

    is_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'main_reservations'
        ordering = ('-date_created',)

