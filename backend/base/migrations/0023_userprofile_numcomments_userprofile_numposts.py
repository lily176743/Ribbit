# Generated by Django 4.1.3 on 2022-12-12 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_subribbit_createdat'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='numComments',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='numPosts',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]