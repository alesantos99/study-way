# Generated by Django 3.0.3 on 2020-03-05 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]