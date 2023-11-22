from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import VideoElement, Votes
from django.core.exceptions import BadRequest
from django.http import HttpResponseBadRequest, HttpResponse, HttpRequest
from django.contrib.auth import get_user # Here
from django.db.models import Count

# Create your views here.

def video_page(request: HttpRequest):
    if request.method == "GET":
        elements = VideoElement.objects.all()
        if request.user.is_authenticated:
            print(get_user(request))
            user_voted = len(Votes.objects.filter(voted_by = get_user(request))) > 0
            votes = Votes.objects.all()
        else:
            user_voted= False
        print(elements)
        return render(request, 'votedashboard/video_page.html', {'elements': elements, 'user_voted': user_voted})
    elif request.method == "POST":
        print(request.body)
        return  HttpResponse("Hello, World!")
def vote(request, video_id):
    if len(Votes.objects.filter(voted_by = get_user(request))) > 0:
        return HttpResponseBadRequest("Este usuario ya ha votado. ¿Qué tramas, moreno?")
    
    user = get_user(request)

    video = get_object_or_404(VideoElement, pk=video_id)
    vote = Votes()
    vote.voted_by = user
    vote.voted_for = video
    video.total_votes += 1
    vote.save()
    video.save()
    return redirect("votedashboard:video_page")
