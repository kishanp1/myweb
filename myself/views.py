from django.http import HttpResponse
from django.shortcuts import render
from .models import Skilltype, Skills
# Create your views here.

def index(request):
    all_skilltype= Skilltype.objects.all()
    all_skillnames= Skills.objects.all()
    context={
            'all_skilltype' : all_skilltype,
            'all_skills': all_skillnames,}

    return render(request,'myself/index.html',context)
