# Generated by Django 3.2.5 on 2021-08-20 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0002_auto_20210820_0351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainer',
            old_name='bank_account',
            new_name='bank_account_number',
        ),
        migrations.AddField(
            model_name='trainer',
            name='course_duration',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trainer',
            name='nationality',
            field=models.CharField(choices=[('=M', 'Kenya'), ('K', 'Uganda'), ('O', 'Sudan')], max_length=10),
        ),
    ]
