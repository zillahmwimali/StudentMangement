from django.db import models
from django.db.models.fields import BigAutoField, CharField, DateField, EmailField

class Student(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    gend=((u'=M',U'Male'),
                (u'K',u'Female'),
                (u'O',u'Other'))
    gender=models.CharField(max_length=20,choices=gend)
    email=models.EmailField()
    lang=((u'E',U'English'),
                (u'K',u'Kiswahili'),
                (u'O',u'Other')
    )
    languages=  models.CharField(max_length=2 ,choices=lang)
    id_number=models.CharField(max_length=10)
    country=((u'=M',U'Kenyan'),
                (u'K',u'Ugandan'),
                (u'O',u'Sudanese'))
    nationality=models.CharField(max_length=20,choices=country)
    passport_photo=models.ImageField()
    phone_number=models.PositiveIntegerField()
    room_number=models.PositiveSmallIntegerField()
    mentors_name=models.CharField(max_length=20)
    class_name=models.CharField(max_length=10)
    medical_report=models.FileField()
    laptop_serial=models.CharField(max_length=10)
    big_sister=models.CharField(max_length=20)
    passport_number=models.CharField(max_length=10)
    guardian=models.CharField(max_length=20)
    district=models.CharField(max_length=20)

    def __str__(self):
        return self.first_name