# __ we dont need this cuz we are using microservise in the "djangoapi"

from multiprocessing import context
from urllib import response
from django.shortcuts import render
import requests

# Create your views here.

API_KEY = '1df23db748374ef2a9de84c7f72d2288'

def arti(request):

    country = str(request.GET.get('country')).replace("None", "")
    category = str(request.GET.get('category')).replace("None", "")

    if category or country:

        response = requests.get(f'http://127.0.0.1:8081/test?country={country}&category={category}')
        data = response.json()['articles']

    else:
        data = []

    return render(request, 'NEWS/arti.html', context ={"articles":data})
