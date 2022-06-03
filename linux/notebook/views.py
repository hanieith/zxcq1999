from django.shortcuts import render
from .models import Names
import json
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'POST':
        json_dict = request.POST.dict()
        json_dict.pop('csrfmiddlewaretoken')
        json_resp = json.dumps(json_dict)
        json_save = Names.objects.create(name=json_resp)
        json_save.save()
        return HttpResponseRedirect('/view/')
    else:
        return render(request, template_name='notebook/index.html')


def view_names(request):
    submits = Names.objects.all()
    context = {'names':submits}
    return render(request, template_name='notebook/view_names.html', context=context)
