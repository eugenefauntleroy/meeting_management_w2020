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
        self.meeting= Meeting(meetingtitle='First', meetingdate=self.date, user=self.user, meetingtime=meetingtime.time('2021/1/10'), location='Seattle', agenda='N/A')
    
    def test_string(self):
        self.assertEqual(str(self.meeting), 'First')