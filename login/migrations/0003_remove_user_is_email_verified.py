# Generated by Django 3.2.4 on 2021-07-07 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_user_is_email_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_email_verified',
        ),
    ]