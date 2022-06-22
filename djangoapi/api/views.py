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
    # name = request.POST['u_name'] # u_name is the name of the input tag 
	# age = request.POST['age'] 
	# address = request.POST['address'] 
    
    # country = request.POST['country']
    # newsapi = 'https://newsapi.org/v2/everything?q=tesla&from=2022-04-11&sortBy=publishedAt&apiKey=595ecd51ec474a4aa58cb5ad59e05f93'

    # response = request.GET.get('https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=595ecd51ec474a4aa58cb5ad59e05f93')
    # data = response.json()
    # #country = 'us'
    # #response = requests.get('https://newsapi.org/v2/top-headlines?country='+ country +'&apiKey=595ecd51ec474a4aa58cb5ad59e05f93')
    # #data = json.loads(response.content)

    # names = []
    # for article in data['articles']:
    #     # names.append(article['title'])
    #     names.append(article['description'])
    # context= {'names':names}

    # l = data['articles']
    # desc =[]
    # news =[]
    # img =[]
    # url =[]
  
    # for i in range(len(l)):
    #     f = l[i]
    #     news.append(f['title'])
    #     desc.append(f['description'])
    #     img.append(f['urlToImage'])
    #     url.append(f['url'])

    # mylist = zip(news, desc, img, url)
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

    # articles = []
    # for article in data['articles']:
    #     articles.append(article['author'])
    # context={
    #     'author':articles
    # }

    # response = requests.get("http://127.0.0.1:8081/test")
    # print(response.text)
    # data = json.loads(response.content)
    # print(data['mylist'])

    # context = {}
    # return HttpResponse(response.text)
    # return render(request,'NEWS/arti.html', context)


