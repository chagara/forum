from django.shortcuts import render, get_object_or_404
from .models import Section, Category, Thread


def home(request):
    sections = Section.objects.all()
    context = {'sections': sections}
    return render(request, 'forum/home.html', context)


def section_view(request, section_id):
    # This gets all categories which is wrong. It should only get
    # categories for that specific section
    context = {
        "section": get_object_or_404(Section, pk=section_id),
        "categories": Category.objects.all()
    }
    return render(request, 'forum/section.html', context)


def category_view(request, category_id):
    context = {
        "category": get_object_or_404(Category, pk=category_id),
        "threads": Thread.objects.filter(category__pk=category_id)
    }
    return render(request, 'forum/category.html', context)
