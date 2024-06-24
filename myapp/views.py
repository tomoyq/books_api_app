from django.shortcuts import render
from django.views.generic import View
from .forms import SerchForm
import json
import requests

SERCH_URL = 'https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404?format=json&applicationId=1032666932126544202'

def get_api_data(params):
    api = requests.get(SERCH_URL, params=params).text
    result = json.loads(api)
    items = result['Items']
    return items

class IndexView(View):
    def get(self, request, *args, **kwargs):
        form = SerchForm(request.POST or None)

        return render(request, 'myapp/index.html',{
            'form':form,
        })
    
    def post(self, request, *args, **kwargs):
        form = SerchForm(request.POST or None)

        if form.is_valid():
            keyword = form.cleaned_data('title')
            params = {
                'title': keyword,
                'hits': 28,
            }
            items = get_api_data(params)
            book_list = []
            for i in items:
                item = i['Item']
                
