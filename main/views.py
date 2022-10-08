from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


# Create your views here.
class PupilPageView(ListView):
    model = BestPupil
    template_name = "pupils.html"

class TeachersPageView(ListView):
    model = Teacher
    template_name = "teachers.html"



class HomesPageView(ListView):
    model = Home
    template_name = "home.html"

# def HomesPageView(request):
#     data = {
#         "home" : Home.objects.all()
#     }
#     return render(request, 'home.html', data)

class BlogsPageView(ListView):
    model = Blog
    template_name = "blogs.html"


def PostDetail(request, a):
    data = {
        "post": Blog.objects.get(id=a)
    }
    return render(request, "post_detail.html", data)