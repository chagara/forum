from django.shortcuts import render, get_object_or_404
from .models import Section


def home(request):
    sections = Section.objects.all()
    context = {'sections': sections}
    return render(request, 'forum/home.html', context)


def section_view(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    context = {"section": section}
    return render(request, 'forum/section.html', context)
