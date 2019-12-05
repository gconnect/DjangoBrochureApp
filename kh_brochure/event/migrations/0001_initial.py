# Generated by Django 2.2.6 on 2019-10-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('event_image', models.FileField(upload_to='uploads')),
                ('event_date', models.DateTimeField(verbose_name='Event Date')),
                ('created_at', models.DateTimeField(verbose_name='published date')),
            ],
        ),
    ]