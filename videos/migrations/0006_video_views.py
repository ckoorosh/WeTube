# Generated by Django 4.0.6 on 2022-07-24 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_comment_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
