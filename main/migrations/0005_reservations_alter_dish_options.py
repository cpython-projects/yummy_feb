# Generated by Django 5.1.6 on 2025-03-10 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('number_guests', models.PositiveSmallIntegerField(default=1)),
                ('message', models.TextField(max_length=255)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'main_reservations',
                'ordering': ('-date_created',),
            },
        ),
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ('sort', 'name'), 'verbose_name': 'Dish', 'verbose_name_plural': 'Dishes'},
        ),
    ]
