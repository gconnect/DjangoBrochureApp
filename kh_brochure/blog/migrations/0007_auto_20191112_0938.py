# Generated by Django 2.2.6 on 2019-11-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191112_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=200), max_length=200),
        ),
    ]