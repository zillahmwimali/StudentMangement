# Generated by Django 3.2.5 on 2021-08-20 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_code',
            new_name='unit',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='unit_name',
            new_name='unit_language',
        ),
        migrations.RemoveField(
            model_name='course',
            name='syllabus',
        ),
        migrations.AddField(
            model_name='course',
            name='course_material',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='course',
            name='course_syllabus',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='course',
            name='course_title',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='trainers_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='unit_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_schedule',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
