# Generated by Django 2.2.13 on 2020-06-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='/images/'),
        ),
    ]
