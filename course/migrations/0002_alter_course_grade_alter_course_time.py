# Generated by Django 4.1.5 on 2023-01-14 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='grade',
            field=models.IntegerField(max_length=4),
        ),
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.DateTimeField(),
        ),
    ]