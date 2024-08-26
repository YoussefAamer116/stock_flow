from django.urls import path
from . import views
urlpatterns = [
    path('sell-item/', views.sell_item, name='sell_item'),
    path('sales-report/', views.sales_report, name='sales_report'),
]
