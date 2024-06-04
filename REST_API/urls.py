
from django.urls import include, path
from .views import *



urlpatterns=[
    path('',get_data,name="get_data"),
    path('product',view=create_book,name="product"),
    path('create_book',view=create_single_book,name="create_single_book"),
    path('single_book/<str:id>/',view=get_single_book,name="single_book"),
    path('edit_book/<str:id>/',view=edit_book,name="edit_book"),
]