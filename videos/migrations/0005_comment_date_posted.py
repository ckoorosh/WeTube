# Generated by Django 4.0.6 on 2022-07-24 17:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_alter_video_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]