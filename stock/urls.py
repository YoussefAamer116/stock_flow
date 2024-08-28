from django.urls import path
from . import views
urlpatterns = [
    path('add-item/', views.add_item, name='add_item'),
    
]
