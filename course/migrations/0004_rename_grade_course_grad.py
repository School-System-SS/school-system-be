# Generated by Django 4.1.5 on 2023-01-14 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_course_grade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='grade',
            new_name='grad',
        ),
    ]