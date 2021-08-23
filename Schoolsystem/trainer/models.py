from django.db import models
from django.db.models.fields import BigAutoField, CharField, DateField, EmailField

class Trainer(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    country=((u'=M',U'Kenyan'),
                (u'K',u'Ugandan'),
                (u'O',u'Sudanese'))
    nationality=models.CharField(max_length=10,choices=country)
    gend=((u'=M',U'Male'),
                (u'K',u'Female'),
                (u'O',u'Other'))
    gender=models.CharField(max_length=20,choices=gend)
    age=models.CharField(max_length=12)
    id_number=models.CharField(max_length=12)
    phone_number=models.PositiveIntegerField()
    email=models.EmailField()
    profession=models.CharField(max_length=20)
    company=models.CharField(max_length=20)
    job_title=models.CharField(max_length=10)
    unit=models.CharField(max_length=20)
    unit_code=models.CharField(max_length=10)
    lessons_per_month=models.PositiveSmallIntegerField()
    course_duration=models.PositiveSmallIntegerField()
    syllabus=models.FileField()
    contract=models.FileField()
    bank_account_number=models.CharField(max_length=16,)
    resume=models.FileField()
    photo=models.ImageField()

    def __str__(self):
        return self.first_name