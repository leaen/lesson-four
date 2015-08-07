from django.shortcuts import render, get_object_or_404

from .models import Client, Entry, Project


def clients(request):
    client_list = Client.objects.all()
    return render(request, 'clients.html', {
        'client_list': client_list,
    })


def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'client_detail.html', {
        'client': client,
    })


def entries(request):
    entry_list = Entry.objects.all()
    return render(request, 'entries.html', {
        'entry_list': entry_list,
    })


def projects(request):
    project_list = Project.objects.all()
    return render(request, 'projects.html', {
        'project_list': project_list,
    })
