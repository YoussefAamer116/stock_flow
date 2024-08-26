from django.urls import path
from . import views
urlpatterns = [
    path('sell-item/', views.sell_item, name='sell_item'),
]
