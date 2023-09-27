# Generated by Django 3.2.4 on 2022-12-07 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]