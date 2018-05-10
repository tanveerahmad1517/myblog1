# Generated by Django 2.0 on 2018-04-30 07:45

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_post_title_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='media/default.png', upload_to=posts.models.get_image_path),
        ),
    ]