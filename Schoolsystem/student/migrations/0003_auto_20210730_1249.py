# Generated by Django 3.2.5 on 2021-07-30 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_nationality'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Big_sister',
            new_name='big_sister',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Class_name',
            new_name='class_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Date_of_birth',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='District',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='First_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Guardian',
            new_name='guardian',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='ID_number',
            new_name='id_number',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Languages',
            new_name='languages',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Laptop_serial',
            new_name='laptop_serial',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Medical_report',
            new_name='medical_report',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Mentors_name',
            new_name='mentors_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Nationality',
            new_name='nationality',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Passport_number',
            new_name='passport_number',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Passport_photo',
            new_name='passport_photo',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Phone_number',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Room_number',
            new_name='room_number',
        ),
    ]
