from django.shortcuts import render, get_object_or_404
from .models import Section, Category


def home(request):
    sections = Section.objects.all()
    context = {'sections': sections}
    return render(request, 'forum/home.html', context)


def section_view(request, section_id):
    context = {
        "section": get_object_or_404(Section, pk=section_id),
        "categories": Category.objects.all()
    }
    return render(request, 'forum/section.html', context)
