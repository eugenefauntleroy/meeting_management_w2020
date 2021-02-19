from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy
from .forms import meetingForm 
# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def meetings(request):
    meetingtitle = Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meetingtitle': meetingtitle})

def meetingdetail(request, id):
    meeting=get_object_or_404(Meeting, pk=id) #"Meeting" is capitalized
    return render(request, 'club/meetingdetail.html', {'meeting' : meeting})

def newMeeting(request):
    form=meetingForm

    if request.method=='POST':
        form=meetingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form=meetingForm()
    
    else:
        form=meetingForm()
    return render(request,'club/meetings.html', {'form' : form})


    
