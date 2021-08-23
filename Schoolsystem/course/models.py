from django.db import models

class Course(models.Model):
    course_name=models.CharField(max_length=20,null=True,blank=True)
    course_schedule=models.CharField(max_length=20,null=True,blank=True)
    unit=models.CharField(max_length=20,null=True)
    unit_code=models.CharField(max_length=20,null=True,blank=True)
    unit_language=models.CharField(max_length=20,null=True)
    duration=models.DurationField(null=True,blank=True)
    course_syllabus=models.FileField(null=True,blank=True)
    course_material=models.FileField(null=True,blank=True)
    trainers_name=models.CharField(max_length=20)

    def __str__(self):
        return self.course_name