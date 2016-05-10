from django.shortcuts import render, get_object_or_404
from .models import Section, Category, Thread, Comment


def home(request):
    context = {
        "page_title": "DjangoLearners",
        "children": Section.objects.all(),
        "child_class": "section",
        "child_url": "forum:section_view"
    }
    return render(request, 'forum/overview.html', context)


def section_view(request, pk):
    section = get_object_or_404(Section, pk=pk)
    context = {
        "page_title": section.name,
        "child_class": "category",
        "children": Category.objects.filter(section__pk=pk),
        "child_url": "forum:category_view"
    }
    return render(request, 'forum/overview.html', context)


def category_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    context = {
        "page_title": category.name,
        "child_class": "thread",
        "child_url": "forum:thread_view",
        "children": Thread.objects.filter(category__pk=pk)
    }
    return render(request, 'forum/overview.html', context)


def thread_view(request, pk):
    context = {
        "thread": get_object_or_404(Thread, pk=pk),
        "comments": Comment.objects.filter(thread__pk=pk)
    }
    return render(request, 'forum/thread.html', context)
