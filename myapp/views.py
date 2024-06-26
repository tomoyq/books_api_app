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
            keyword = form.cleaned_data['title']
            params = {
                'title': keyword,
                'hits': 28,
            }
            items = get_api_data(params)
            book_list = []
            for i in items:
                item = i['Item']
                title = item['title']
                image = item['largeImageUrl']
                isbn = item['isbn']
                query = {
                    'title': title,
                    'image': image,
                    'isbn': isbn,
                }
                book_list.append(query)
            
            return render(request, 'myapp/book.html', {
                'book_list': book_list,
                'keyword':keyword,
            })
        return render(request, 'myapp/index.html', {
            'form': form,
        })
    
class DetailView(View):
    def get(self, request, *args, **kwargs):
        isbn = self.kwargs['isbn']
        params = {
            'isbn': isbn
        }

        items = get_api_data(params)
        items = items[0]
        item = items['Item']
        title = item['title']
        image = item['largeImageUrl']
        author = item['author']
        itemPrice = item['itemPrice']
        salesDate = item['salesDate']
        publisherName = item['publisherName']
        size = item['size']
        isbn = item['isbn']
        itemCaption = ['itemCaption']
        itemUrl = item['itemUrl']
        reviewAverage = item['reviewAverage']
        reviewCount = item['reviewCount']

        book_list = {
            'title': title,
            'image': image,
            'author': author,
            'itemPrice': itemPrice,
            'salesDate': salesDate,
            'publisherName': publisherName,
            'size': size,
            'isbn': isbn,
            'itemCaption': itemCaption,
            'itemUrl': itemUrl,
            'reviewAverage': reviewAverage,
            'reviewCount': reviewCount,
            'average': float(reviewAverage) * 20
        }

        return render(request, 'myapp/detail.html', {
            'book_list': book_list,
            })
