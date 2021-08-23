from django.db import models


class Calendar(models.Model):
    event_name=models.CharField(max_length=20)
    event_id=models.CharField(max_length=20,null=True,blank=True)
    event_date=models.DateTimeField() 
    event_agenda=models.CharField(max_length=30,null=True,blank=True)
    event_venue=models.CharField(max_length=10,null=True,blank=True)
    event_duration=models.DurationField(null=True,blank=True)
    number_of_event_attendees=models.BigIntegerField()
    event_planner=models.CharField(max_length=10,null=True,blank=True)
    event_activity=models.CharField(max_length=10,null=True,blank=True)
    event_approved_by=models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.event_name