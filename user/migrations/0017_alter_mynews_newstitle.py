# Generated by Django 3.2.4 on 2023-05-16 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20230506_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mynews',
            name='newstitle',
            field=models.CharField(max_length=200),
        ),
    ]
