# Generated by Django 3.2.4 on 2022-12-07 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='Message',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='number',
            new_name='Number',
        ),
    ]