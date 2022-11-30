from django.shortcuts import render
from django.http import HttpResponse
from search import settings
from .service import RetriveResults


# Create your views here.

def search(request):
    return render(request, 'search.html')

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
