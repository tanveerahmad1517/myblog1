# Generated by Django 2.0 on 2018-05-09 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_auto_20180509_2146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='users',
        ),
    ]