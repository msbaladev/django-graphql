from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *


@api_view(['GET'])
def get_data(request):
    try:
        data=products.objects.all().values()
        print(data)
        return JsonResponse({"data":list(data),},safe=False)
    except Exception as e:
        return JsonResponse({"message":"oops!,Something went Wrong"})
       
       
       
@api_view(['POST'])
def create_products(request):
    try:
       data=request.data
       print(data)
       return JsonResponse({"message":"Item created successfully"})
       
    except Exception as e:
       return JsonResponse({"message":"Something went Wrong"})
        
        
        
       
       
       
       
       
       
       
       
       
       
       