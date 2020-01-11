from django.http import HttpResponse
from django.shortcuts import render
from event.models import Event
from member.models import Member
# Create your views here.
def homepage(request):
    events=Event.objects
    members=Member.objects
    return render(request,'index.html',{'events':events,'members':members})