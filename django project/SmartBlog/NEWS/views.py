from multiprocessing import context
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
import requests
# from newsapi import NewsApiClient

# Create your views here.

API_KEY = '595ecd51ec474a4aa58cb5ad59e05f93'

def arti(request):
    # data = response.json()
    # country = requests.post('us')
    country = str(request.GET.get('country')).replace("None", "")
    category = str(request.GET.get('category')).replace("None", "")

    if category or country:

        response = requests.get(f'http://127.0.0.1:8081/test?country={country}&category={category}')
        # response = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=595ecd51ec474a4aa58cb5ad59e05f93')
        data = response.json()['articles']
        # print(data)

    else:
        data = []

    return render(request, 'NEWS/arti.html', context ={"articles":data})
