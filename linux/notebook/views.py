from django.shortcuts import render
from .models import Names

def index(request):
    name = 'hanieith'
    context = {
        'name':name
    }
    return render(request, template_name='notebook/index.html', context=context)

def view_names(request):
    return render(request, template_name='notebook/view_names.html')