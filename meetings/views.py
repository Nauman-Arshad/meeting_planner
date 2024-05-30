from django.shortcuts import render, get_object_or_404
from .models import Meeting

def meetings(request):
    meetings = Meeting.objects.all()
    return render(request, 'meetings/meetings.html', {'meetings': meetings})

def meeting_detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/detail.html', {'meeting': meeting})

