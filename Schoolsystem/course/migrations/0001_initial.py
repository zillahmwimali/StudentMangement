# Generated by Django 3.2.5 on 2021-08-20 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=20, null=True)),
                ('course_name', models.CharField(max_length=20, null=True)),
                ('course_code', models.CharField(max_length=20, null=True)),
                ('course_schedule', models.CharField(max_length=20, null=True)),
                ('syllabus', models.TextField(null=True)),
            ],
        ),
    ]
