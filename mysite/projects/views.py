from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Item


def index(request):
    projects = Item.objects.all().order_by('-pub_date')
    context = {'projects': projects}
    return render(request, 'index.html', context)


def projects(request, slug):
    project = Item.objects.filter(slug=slug)
    context = {'project': project[0]}
    return render(request, 'projects/projects.html', context)


def get_all_posts(request):
    items = Item.objects.all().defer('content')
    items = serializers.serialize("json", items, use_natural_foreign_keys=True)

    return HttpResponse(items, content_type="application/json")
