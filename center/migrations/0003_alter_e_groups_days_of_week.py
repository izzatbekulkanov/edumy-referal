# Generated by Django 5.0.6 on 2024-11-08 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0002_e_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='e_groups',
            name='days_of_week',
            field=models.JSONField(blank=True, default=list, help_text='Hafta kunlarini tanlang', verbose_name='Dars kunlari'),
        ),
    ]
