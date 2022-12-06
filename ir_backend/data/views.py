from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from data.service import DataService
import time

# Create your views here.
@api_view(['POST'])
def insert_data(request):
  data_service = DataService()
  try:
    no_data_inserted = data_service.create_index()
    return Response({'No of data inserted': no_data_inserted}, status=status.HTTP_201_CREATED)
  except Exception as err:
    return Response({'Error Message': err}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def insert_data(request):
  data_service = DataService()
  try:
    data_service.insert_data()
    time.sleep(2)
    data_service.insert_tf_idf_data()
    time.sleep(2)
    data_service.insert_auto_data()
    return Response({'status': 'Data inserted successfully.'}, status=status.HTTP_201_CREATED)
  except Exception as err:
    return Response({'Error Message': err}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def insert_auto_suggestion_data(request):
  data_service = DataService()
  try:
    no_data_inserted = data_service.insert_auto_data()
    return Response({'No of data inserted': no_data_inserted}, status=status.HTTP_201_CREATED)
  except Exception as err:
    return Response({'Error Message': err}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def insert_tf_idf_data(request):
  data_service = DataService()
  try:
    no_data_inserted = data_service.insert_tf_idf_data()
    return Response({'No of data inserted': no_data_inserted}, status=status.HTTP_201_CREATED)
  except Exception as err:
    return Response({'Error Message': err}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
