# Generated by Django 4.0.3 on 2022-05-23 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_user_alter_post_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.CharField(max_length=60),
        ),
    ]
