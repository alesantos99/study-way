# Generated by Django 3.0.3 on 2020-05-28 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='themes',
            field=models.ManyToManyField(to='core.Theme'),
        ),
    ]
