# Generated by Django 4.2.6 on 2023-10-19 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={},
        ),
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.RemoveField(
            model_name='book',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
        migrations.RemoveField(
            model_name='book',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='book',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='book',
            name='updated_up',
        ),
    ]
