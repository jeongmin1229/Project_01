# Generated by Django 3.2.13 on 2022-05-23 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='review_count',
            field=models.CharField(default='', max_length=200),
        ),
    ]