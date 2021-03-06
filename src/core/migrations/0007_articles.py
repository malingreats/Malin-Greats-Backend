# Generated by Django 3.2.7 on 2021-10-13 17:46

import core.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_siteimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('excerpt', models.TextField()),
                ('content1', models.TextField(blank=True)),
                ('content2', models.TextField(blank=True)),
                ('content3', models.TextField(blank=True)),
                ('content4', models.TextField(blank=True)),
                ('subContent1', models.TextField(blank=True)),
                ('subContent2', models.TextField(blank=True)),
                ('image1', models.ImageField(upload_to=core.models.upload_to)),
                ('image2', models.ImageField(upload_to=core.models.upload_to)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('publishedDay', models.DateField(default=2)),
            ],
        ),
    ]
