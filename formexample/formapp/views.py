from django.shortcuts import render
from django import forms


class HelloWorldForm(forms.Form):
    name = forms.CharField()


def example(request):
    return render(request, 'form.html')


def django_example(request):
    form = HelloWorldForm()
    return render(request, 'django_form.html', {
        'form': form,
    })
