# Generated by Django 4.2.1 on 2023-05-12 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_rename_author_photo_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]
