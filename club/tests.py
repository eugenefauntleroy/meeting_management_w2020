from django.test import TestCase
from django.contrib.auth.models import User
from . models import Meeting, MeetingMinutes, Resource, Event
import datetime
# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.meeting=Meeting(meetingtitle='First Meeting')
    
    def test_meetingstring(self):
        self.assertEqual(str(self.meeting), 'First Meeting')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class DateTest(TestCase):
    def setup(self):
        self.user=User(username='user1')
        self.meeting=Meeting(meetingtitle='First', user=self.user, meetingdate=self.date('2021,1,10'), meetingtime=self.time('00:00:00'), location='Seattle', agenda='N/A')
        #self.meeting=Meeting(meetingdate=self.date('2021,1,10')
    def test_string(self):  
        self.assertEqual(str(self.meeting),'First')
    
    def test_resource(self):
        rec = self.resource 
        self.assertEqual(self.resource(),rec)

    def test_event(self):
        self.assertEqual(self.event)
 