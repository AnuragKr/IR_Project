from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from data.service import DataService

# Create your views here.
@api_view(['POST'])
def insert_data(request):
  data_service = DataService()
  try:
    no_data_inserted = data_service.create_index()
    return Response({'No of data inserted': no_data_inserted}, status=status.HTTP_201_CREATED)
  except Exception as err:
    return Response({'Error Message': err}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
