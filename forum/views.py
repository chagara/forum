from django.shortcuts import render, get_object_or_404
from .models import Section, Category, Thread, Comment


def home(request):
    sections = Section.objects.all()
    context = {'sections': sections}
    return render(request, 'forum/home.html', context)


def section_view(request, section_id):
    context = {
        "section": get_object_or_404(Section, pk=section_id),
        "categories": Category.objects.filter(section__pk=section_id)
    }
    return render(request, 'forum/detail.html', context)


def category_view(request, category_id):
    context = {
        "category": get_object_or_404(Category, pk=category_id),
        "threads": Thread.objects.filter(category__pk=category_id)
    }
    return render(request, 'forum/category.html', context)


def thread_view(request, thread_id):
    context = {
        "thread": get_object_or_404(Thread, pk=thread_id),
        "comments": Comment.objects.filter(thread__pk=thread_id)
    }
    return render(request, 'forum/thread.html', context)
