# Generated by Django 4.0.3 on 2022-05-23 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_alter_post_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
    ]
