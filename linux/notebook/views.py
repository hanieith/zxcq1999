from django.shortcuts import render

def index(request):
    name = 'hanieith'
    context = {
        'name':name
    }
    return render(request, template_name='notebook/index.html', context=context)