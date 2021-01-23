from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Meeting(models.Model):
    meetingtitle = models.CharField(max_length=255)
    meetingdate = models.DateTimeField()
    meetingtime = models.TimeField()
    location = models.CharField(max_length=255)
    agenda = models.CharField(max_length=255)

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table="meeting"

class MeetingMinutes(models.Model):
    meetingid = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    attendance = models.ManyToManyField(User)
    minutes = models.TimeField()
    
    def __str___(self):
        return self.meetingid 
    
    class Meta:
        db_table = 'meeting minutes'

class Resource(models.Model):
    resourcename = models.CharField(max_length=255)
    resourcetype = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    URL = models.URLField()
    dateentered = models.DateField()
    userid = models.ManyToManyField(User)

    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table = 'resource'

class Event(models.Model):
    eventtitle = models.CharField(max_length=255)
    locationdate = models.DateField()
    time = models.TimeField()
    description = models.TextField(null=True, blank=True)
    userid = models.ManyToManyField(User)

    def __str__(self):
        return self.eventtitle
    
    class Meta:
        db_table = 'event'