from multiprocessing import context
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
import requests

# Create your views here.

API_KEY = '1df23db748374ef2a9de84c7f72d2288'

def arti(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/everything?q={category}&sortBy=relevancy&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    context = {
        'articles' : articles
    }
    print(articles)
    return JsonResponse(context)

