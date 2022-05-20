# Generated by Django 4.0.4 on 2022-05-20 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('scope', models.CharField(max_length=10, verbose_name='별점')),
                ('register_dttm', models.CharField(max_length=100, verbose_name='등록날짜')),
            ],
            options={
                'verbose_name': '리뷰',
                'verbose_name_plural': '리뷰',
            },
        ),
    ]
