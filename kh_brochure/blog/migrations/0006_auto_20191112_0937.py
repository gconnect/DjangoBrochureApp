# Generated by Django 2.2.6 on 2019-11-12 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='title', max_length=200),
        ),
    ]