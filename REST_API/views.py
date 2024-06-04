from django.http import HttpResponse, JsonResponse
from rest_framework import status
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *
import pandas


@api_view(['GET'])
def get_data(request):
    try:
        data=icc.objects.all().values()
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
   
   
   
# @api_view(['POST'])
# def create_book(request):
#    try:
#       serializer = ProductSerializer(data=request.data)
#       if serializer.is_valid():
#          serializer.save()
#          return JsonResponse({"message":serializer.data},status=status.HTTP_201_CREATED)
#       return JsonResponse({"message":serializer.error})
#    except Exception as e:
#       return JsonResponse({"message":"something went wrong"})  
   
@api_view(['POST'])
def create_book(request):
   try:
      if request.method == "POST":
         name=request.POST.get('name')
         file=request.FILES['file']
         sheet1 = pandas.read_excel(file)
         data = sheet1.to_dict(orient='records')
         print(data)
         for item in data:
            icc_data=icc(
               category=item['Category'],
               qpn=item['QPN'],
               part_no=item['Netapp PN'],
            )
            icc_data.save()
         return JsonResponse({"message":"success","data":data})  
   except Exception as e:
      return JsonResponse({"message":"something went wrong"})       
        
        
        
       
@api_view(['POST'])    
def create_single_book(request):
   
    try:
      if request.method == "POST":
         title=request.data['name']
         print(title)
         
         
         data=icc(
            category=title
         )
         data.save()
         
      return JsonResponse({"message":"created successfully"})
    except Exception as error:
      return JsonResponse({"message":str(error)})
   
 

@api_view(['GET']) 
def get_single_book(request,id):
  
   try:
     
      data=icc.objects.filter(id=id).values()
      print(data)
      return JsonResponse({"data":list(data)})
   except Exception as error:
      return JsonResponse({"message":str(error)})
   


@api_view(['PUT'])
def edit_book(request,id):
   try:
     if request.method == "PUT":
        category=request.data['category']
        print(request.data)
        
        data=icc.objects.filter(id=id).update(category=category)
        return JsonResponse({"message":"updated successfully"})
       
   except Exception as error:
       return JsonResponse({"message":str(error)})
       
       
       
       
       
       
       