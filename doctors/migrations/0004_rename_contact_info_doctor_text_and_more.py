# Generated by Django 4.2.16 on 2024-10-27 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_alter_doctor_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='contact_info',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='specialty',
        ),
    ]