# Generated by Django 4.0.4 on 2023-12-09 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_commonfeatures_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(db_index=True, max_length=30, null=True, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=14, verbose_name='phone number'),
        ),
    ]