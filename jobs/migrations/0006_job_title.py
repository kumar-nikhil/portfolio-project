# Generated by Django 2.2.13 on 2020-06-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20200606_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='title', max_length=100),
        ),
    ]