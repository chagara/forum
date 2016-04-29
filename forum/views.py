from django.shortcuts import render, get_object_or_404
from .models import Section, Category, Thread, Comment


def home(request):
    context = {
        "page_title": "DjangoLearners",
        "children": Section.objects.all(),
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
    context = {
        "category": get_object_or_404(Category, pk=pk),
        "threads": Thread.objects.filter(category__pk=pk)
    }
    return render(request, 'forum/category.html', context)


def thread_view(request, thread_id):
    context = {
        "thread": get_object_or_404(Thread, pk=thread_id),
        "comments": Comment.objects.filter(thread__pk=thread_id)
    }
    return render(request, 'forum/thread.html', context)
