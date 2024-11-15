# Generated by Django 5.0.6 on 2024-11-08 14:04

import django.contrib.auth.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cashback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Cashback turi')),
                ('type', models.CharField(choices=[('1', 'Kirish'), ('2', "O'qituvchi"), ('3', "O'quvchi"), ('4', 'Admin')], max_length=20, verbose_name='Turi')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Tuman kodi')),
                ('name', models.CharField(max_length=255, verbose_name='Tuman nomi')),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Jins kodi')),
                ('name', models.CharField(max_length=255, verbose_name='Jins nomi')),
            ],
        ),
        migrations.CreateModel(
            name='Quarters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Mahalla kodi')),
                ('name', models.CharField(max_length=255, verbose_name='Mahalla nomi')),
            ],
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Viloyat kodi')),
                ('name', models.CharField(max_length=255, verbose_name='Viloyat nomi')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='role kodi')),
                ('name', models.CharField(max_length=255, verbose_name='role nomi')),
            ],
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Kirish vaqti')),
                ('logout_time', models.DateTimeField(blank=True, null=True, verbose_name='Chiqish vaqti')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ism')),
                ('second_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Familia')),
                ('third_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Otasining ismi')),
                ('p_first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ota onasining ismi')),
                ('p_second_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ota onasining familiya')),
                ('p_phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Ota onasining telefon raqami')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name="Tug'ilgan kun")),
                ('imageFile', models.ImageField(blank=True, default='default/user.png', null=True, upload_to='students/%Y/%m/%d', verbose_name='Rasmi faylda')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Manzili')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqti")),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name="So'nggi kirish vaqti")),
                ('last_logout', models.DateTimeField(blank=True, null=True, verbose_name="So'nggi chiqish vaqti")),
                ('now_role', models.CharField(blank=True, max_length=255, null=True, verbose_name='Foydalanuvchining hozirgi vaqtdagi roli')),
                ('username', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('password_save', models.CharField(blank=True, max_length=128, null=True, verbose_name='password save')),
                ('user_type', models.CharField(blank=True, choices=[('1', "O'quvchi"), ('2', "O'qituvchi"), ('3', 'Direktor'), ('4', 'Administrator'), ('5', 'CEO_Administrator')], default='1', max_length=20, null=True, verbose_name='Type')),
                ('is_active', models.BooleanField(default=True)),
                ('passport_serial', models.CharField(blank=True, max_length=20, null=True)),
                ('passport_jshshir', models.CharField(blank=True, max_length=20, null=True)),
                ('telegram', models.URLField(blank=True, null=True, verbose_name='Telegram profil havolasi')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram profil havolasi')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook profil havolasi')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
