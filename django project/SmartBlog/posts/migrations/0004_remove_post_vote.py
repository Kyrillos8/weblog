# Generated by Django 4.0.3 on 2022-05-08 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='vote',
        ),
    ]
