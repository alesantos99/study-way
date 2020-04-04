# Generated by Django 3.0.3 on 2020-03-30 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200329_2057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='USERNAME_FIELD',
            new_name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
