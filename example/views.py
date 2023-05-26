# example/views.py
from datetime import datetime

from django.shortcuts import render

def index(request):
    now = datetime.now()
    return render(request, "example/index.html", {
        now: now.strftime("%b %dth, %Y - %H:%M hrs")
    })
    