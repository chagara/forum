from django.shortcuts import render
from .models import Section


def home(request):
    sections = Section.objects.all()
    context = {'sections': sections}
    return render(request, 'forum/home.html', context)


def section_view(request, section_id):
    return render(request, 'forum/section.html')
