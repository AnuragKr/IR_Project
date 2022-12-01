from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from search.service import SearchService
# Create your views here.

@api_view(['GET'])
def get_bm25_text_field_result(request):
    query = request.data['query']
    if query is None:
        return Response("Parameter is missing", status=status.HTTP_400_BAD_REQUEST)
    search_service = SearchService()
    try:
        result = search_service.search_text_field_bm25(query)
        return Response(result, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'Error Message': err}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
