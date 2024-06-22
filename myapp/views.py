from django.shortcuts import render
from django.views.generic import View
from .forms import SerchForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        form = SerchForm(request.POST or None)

        return render(request, 'myapp/index.html',{
            'form':form,
        })
