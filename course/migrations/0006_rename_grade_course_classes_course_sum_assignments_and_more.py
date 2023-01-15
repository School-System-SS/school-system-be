# Generated by Django 4.1.5 on 2023-01-15 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_rename_grad_course_grade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='grade',
            new_name='classes',
        ),
        migrations.AddField(
            model_name='course',
            name='sum_assignments',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]