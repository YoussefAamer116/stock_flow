from django.urls import path
from . import views
urlpatterns = [
    path('', views.stock_page, name='stock_page'),
    path('add-item/', views.add_item, name='add_item'),
    
]
