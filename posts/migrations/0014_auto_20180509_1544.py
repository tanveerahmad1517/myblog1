# Generated by Django 2.0 on 2018-05-09 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20180509_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]