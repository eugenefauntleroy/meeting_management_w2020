from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def meetings(request):
    meetingtitle = Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meetingtitle': meetingtitle})

def meetingdetail(request, id):
    meeting=get_object_or_404(Meeting, pk=id) #"Meeting" is capitalized
    return render(request, 'club/meetingdetail.html', {'meeting' : meeting})