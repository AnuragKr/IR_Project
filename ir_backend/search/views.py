from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from search.service import SearchService
import json
# Create your views here.

@api_view(['GET'])
def get_bm25_text_result(request):
    query = request.GET.get('query', None)
    if query is None:
        return Response("Parameter is missing", status=status.HTTP_400_BAD_REQUEST)
    search_service = SearchService()
    try:
        result = search_service.search_text_bm25(query)
        return Response(result, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'Error Message': err}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_tf_idf_text_result(request):
    query = request.GET.get('query', None)
    if query is None:
        return Response("Parameter is missing", status=status.HTTP_400_BAD_REQUEST)
    search_service = SearchService()
    try:
        result = search_service.search_text_tf_idf(query)
        return Response(result, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'Error Message': err}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_bm25_fuzzy_text_result(request):
    query = request.GET.get('query', None)
    if query is None:
        return Response("Parameter is missing", status=status.HTTP_400_BAD_REQUEST)
    search_service = SearchService()
    try:
        result = search_service.search_fuzzy_text_bm25(query)
        return Response(result, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'Error Message': err}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def get_bm25_search_suggestion(request):
    query = request.GET.get('query', None)
    if query is None:
        return Response("Parameter is missing", status=status.HTTP_400_BAD_REQUEST)
    search_service = SearchService()
    try:
        result = search_service.search_auto_text_bm25(query)
        return Response(result, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'Error Message': err}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_field_search_result(request):
    if request.body is None:
        return Response("Parameter is missing", status=status.HTTP_400_BAD_REQUEST)
    search_service = SearchService()
    try:
        query_obj = json.loads(request.body.decode("utf-8"))
        result = search_service.search_text_field_bm25(query_obj)
        return Response(result, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'Error Message': err}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_text_result(request):
    if request.body is None:
        return Response("Parameter is missing", status=status.HTTP_400_BAD_REQUEST)
    search_service = SearchService()
    try:
        input_obj = json.loads(request.body.decode("utf-8"))
        print(input_obj)
        if input_obj['model'] == 'bm25':
            if input_obj['is_field_query']:
                result = search_service.search_text_field_bm25(
                    input_obj['query'])
            else:
                result = search_service.search_text_bm25(input_obj['query'])
        else:
            if input_obj['is_field_query']:
                result = search_service.search_text_field_tf_idf(
                    input_obj['query'])
            else:
                result = search_service.search_text_tf_idf(input_obj['query'])
        return Response(result, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'Error Message': err}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

