# Generated by Django 3.2.7 on 2022-04-29 07:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20211013_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgricultureSignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('isFree', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='EducationSignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('isFree', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='RetailSignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('isFree', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.AlterField(
            model_name='articles',
            name='isFeatured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='articles',
            name='publishedDay',
            field=models.DateField(default=4),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Species',
        ),
    ]
