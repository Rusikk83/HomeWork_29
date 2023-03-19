# Generated by Django 4.1.7 on 2023-03-18 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=200)),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
    ]
