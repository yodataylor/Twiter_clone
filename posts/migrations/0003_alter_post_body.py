# Generated by Django 4.1.4 on 2022-12-28 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image_post_likes_alter_post_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(blank=True, db_index=True, max_length=140, null=True, verbose_name='Body'),
        ),
    ]
