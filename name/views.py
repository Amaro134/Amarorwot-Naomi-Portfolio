
from django.shortcuts import render
from django.http import JsonResponse
from .models import Skill, Experience, Project, Stat


def index(request):
    skills_by_category = {
        'frontend': Skill.objects.filter(category='frontend'),
        'backend': Skill.objects.filter(category='backend'),
        'data': Skill.objects.filter(category='data'),
        'tools': Skill.objects.filter(category='tools'),
    }
    context = {
        'skills': skills_by_category,
        'experiences': Experience.objects.all().prefetch_related('bullets'),
        'projects': Project.objects.all().prefetch_related('tags'),
        'stats': Stat.objects.all(),
    }
    return render(request, 'name/index.html', context)
