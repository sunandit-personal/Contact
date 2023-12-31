# Generated by Django 4.0.4 on 2023-12-09 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommonFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('CRT_DT', models.DateTimeField(auto_now_add=True)),
                ('UPDT_DT', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('commonfeatures_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contact.commonfeatures')),
                ('first_name', models.CharField(blank=True, default='', max_length=52, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, default='', max_length=52, verbose_name='Last Name')),
                ('email', models.EmailField(db_index=True, max_length=100, null=True, unique=True, verbose_name='Email')),
                ('phone', models.CharField(blank=True, default='', max_length=100, verbose_name='phone number')),
            ],
            options={
                'ordering': ('first_name',),
            },
            bases=('contact.commonfeatures',),
        ),
    ]
