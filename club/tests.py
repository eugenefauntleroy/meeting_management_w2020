from django.test import TestCase
from . models import Meeting, MeetingMinutes, Resource, Event
# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.meet=Meeting(meetingtitle='First Meeting')
    
    def test_meetingstring(self):
        self.assertEqual(str(self.meet), 'First Meeting')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')