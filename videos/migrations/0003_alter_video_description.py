# Generated by Django 4.0.6 on 2022-07-24 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_video_description_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(default='No description yet ...'),
        ),
    ]
