# Generated by Django 4.2 on 2023-06-15 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st', '0005_students_cgpa1_students_cgpa2_students_cgpa3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='sem',
            field=models.CharField(default=1, max_length=50, null=True),
        ),
    ]
