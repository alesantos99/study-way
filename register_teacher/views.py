from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def register(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'register_teacher/register-teacher.html')