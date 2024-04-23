from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FinancialData
from .serializers import FinancialDataSerializer
from django.http import JsonResponse

import logging

logger = logging.getLogger(__name__)

@api_view(['GET', 'POST'])
def financial_data_list(request):
    """
    List all financial data or create a new financial data entry.
    """
    if request.method == 'GET':
        financial_data = FinancialData.objects.all()
        serializer = FinancialDataSerializer(financial_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FinancialDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def financial_data_detail(request, pk):
    """
    Retrieve, update, or delete a financial data entry.
    """
    try:
        financial_data = FinancialData.objects.get(pk=pk)
    except FinancialData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FinancialDataSerializer(financial_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FinancialDataSerializer(financial_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        financial_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET'])
def calculate_market_value(request):
    """
    Calculate market value for all financial data entries.
    """
    financial_data = FinancialData.objects.all()
    market_values = [{'ISIN': data.ISIN, 'market_value': data.Quantity * data.MarketPrice} for data in financial_data]
    return Response(market_values)

from rest_framework.pagination import PageNumberPagination

# Define a custom pagination class
class CustomPagination(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 100  # Maximum number of items per page


@api_view(['GET'])
def financial_data_list(request):
    paginator = CustomPagination()
    financial_data = FinancialData.objects.all()
    result_page = paginator.paginate_queryset(financial_data, request)
    serializer = FinancialDataSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

def calculate_market_value(request):
    financial_data = FinancialData.objects.all()
    market_values = [
        {
            'ISIN': data.ISIN,
            'Symbol': data.Symbol,
            'MarketValue': data.Quantity * data.MarketPrice  # Calculate market value
        }
        for data in financial_data
    ]
    return JsonResponse(market_values, safe=False)


