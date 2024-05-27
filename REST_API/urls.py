
from django.urls import include, path
from .views import *



urlpatterns=[
    path('',get_data,name="get_data"),
    path('product',view=create_products,name="product")
]