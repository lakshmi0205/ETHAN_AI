from django.urls import path
from . import views

urlpatterns = [
    path('financial_data/', views.financial_data_list),
    path('financial_data/<int:pk>/', views.financial_data_detail),
    path('calculate_market_value/', views.calculate_market_value),
]
