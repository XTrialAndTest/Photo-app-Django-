# Generated by Django 4.2.1 on 2023-05-12 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0005_emailform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailform',
            name='email',
            field=models.CharField(max_length=200),
        ),
    ]