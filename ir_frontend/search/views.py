from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from search import settings
from .service import RetriveResults


# Create your views here.

def search(request):
    return render(request, 'search2.html')

def results(request):
    if request.method == 'POST':
        query = request.POST['query']
        request.session['query'] = query


        get_results = RetriveResults()
        results = get_results.get_results_by_BM25(request.POST)
        
        # print(results)
        # data = {'title':results['search_result'][0]['movie_name'],
        #         'rating':results['search_result'][0]['imdb'],
        #         'year' : results['search_result'][0]['year'],
        #         'plot' : results['search_result'][0][ 'plot'],
        #         'summary' : results['search_result'][0][ 'abstract'],
        # }

        data = results['search_result']

        return render(request, 'results.html', {'query':query, 'data':data})

    if request.method == 'GET':
        query = request.session['query']
        get_results = RetriveResults()
        results = get_results.get_results_by_BM25({'query':query})
        data = results['search_result']
        return render(request, 'results.html', {'query':query, 'data':data})

# /search/?query=

def get_suggesions(request):

    query = request.GET.get('query')
    print(query)

    payloads = ['most popular movies', 'black panther movie', 'most popular actor']


    return JsonResponse({'status':200, 'data':payloads})

def show_results(request):
    query = request.GET.get('query')
    print(query)
    get_results = RetriveResults()
    results = get_results.get_results_by_BM25({'query':query})
    data = results['search_result']
    return render(request, 'results.html', {'query':query, 'data':data})



