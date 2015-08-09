from django.shortcuts import render, get_object_or_404

from .forms import EntryForm
from .forms import ProjectForm
from .forms import ClientForm
from .models import Client, Entry, Project


def clients(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            client = Client()
            client.name = client_form.cleaned_data['name']
            client.save()
    else:
        client_form = ClientForm()

    client_list = Client.objects.all()
    return render(request, 'clients.html', {
        'client_list': client_list,
        'client_form': client_form
    })


def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'client_detail.html', {
        'client': client,
    })


def entries(request):
    if request.method == 'POST':
        # Create our form object with our POST data
        entry_form = EntryForm(request.POST)
        if entry_form.is_valid():
            # If the form is valid, let's create and Entry with the submitted data
            entry = Entry()
            entry.start = entry_form.cleaned_data['start']
            entry.end = entry_form.cleaned_data['end']
            entry.project = entry_form.cleaned_data['project']
            entry.description = entry_form.cleaned_data['description']
            entry.save()
    else:
        entry_form = EntryForm()

    entry_list = Entry.objects.all()
    return render(request, 'entries.html', {
        'entry_list': entry_list,
        'entry_form': entry_form,
    })

def projects(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project = Project()
            project.name = project_form.cleaned_data['name']
            project.client = project_form.cleaned_data['client']
            project.save()
    else:
        project_form = ProjectForm()

    project_list = Project.objects.all()
    return render(request, 'projects.html', {
        'project_list': project_list,
        'project_form': project_form,
    })
