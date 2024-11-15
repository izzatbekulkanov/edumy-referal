# Generated by Django 5.0.6 on 2024-11-08 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Belgisi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=255, verbose_name='Belgisi')),
                ('is_active', models.BooleanField(default=True, verbose_name='Faolmi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqti")),
            ],
        ),
        migrations.CreateModel(
            name='Sinf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=255, verbose_name='Sinfi')),
                ('is_active', models.BooleanField(default=True, verbose_name='Faolmi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqti")),
            ],
        ),
        migrations.CreateModel(
            name='Maktab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maktab_raqami', models.BigIntegerField(verbose_name='Maktab raqami')),
                ('sharntoma_raqam', models.BigIntegerField(verbose_name='Sharntoma raqami')),
                ('is_active', models.BooleanField(default=True, verbose_name='Faolmi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqti")),
                ('belgisi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.belgisi', verbose_name='Belgisi')),
                ('tuman', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.district', verbose_name='Tuman')),
                ('viloyat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.regions', verbose_name='Viloyat')),
                ('sinfi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.sinf', verbose_name='Sinfi')),
            ],
        ),
    ]
