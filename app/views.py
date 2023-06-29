from django.shortcuts import render
from .models import Job

# Create your views here.
def list_jobs:
   all_jobs =Job.objects.all()
   return  render(request,'jobs.html',{'all_jobs':all_jobs})
