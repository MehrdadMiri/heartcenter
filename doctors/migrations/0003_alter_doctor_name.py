# Generated by Django 4.2.16 on 2024-09-21 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_doctor_lang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
