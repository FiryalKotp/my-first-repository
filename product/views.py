from rest_framework import status
from django.http import HttpResponse
from django.shortcuts import render
from product import serializer 
from rest_framework import serializers
from . models import *
from product.serializer import *
from rest_framework.decorators import  api_view 
from rest_framework .response import Response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json
# Create your views here.
import base64
from django.core.files.base import ContentFile
from django.forms.models import model_to_dict
from django.db.models import Prefetch
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import ValidationError




@api_view(['POST'])
def new_item(request, *args, **kwargs): 
    # POST
    if request.method == 'POST':
        try :   
            productSerializer= ProductPostSerializer(data=request.data["product"])
            if productSerializer.is_valid (): 
                product =Product()
                product.ArabicName = request.data['product']['ArabicName']  
                product.EnglishName= request.data['product']['EnglishName']
                product.code =request.data['product']['code']
                product.image =request.data['product']['image']
                product.save()
     
                
            else:
                return Response(productSerializer.errors)
                 
           
        except:
            return Response("Please, enter product ")    
        try:
            categorySerializer = CategorySerializer(data=request.data["category"],many=True)  
            if categorySerializer.is_valid():
  
                pass
            else:
                return Response (categorySerializer.errors)   
            for productCategory in request.data["category"]: 
                category =Category()
                category.name = productCategory["name"]
                category.description =productCategory["description"]
                category.code =productCategory["code"]
                category.product =Product.objects.get(id=product.id)
                category.save()

                
        except:
            return Response("Please, enter product category")
        get_product=Product.objects.get(id=product.id)
        categoryProduct=ProductListSerializer(get_product)
        return Response( categoryProduct.data)
    

           
@api_view(['POST'])
def update_item(request,pk, *args, **kwargs): 
    try :
        get_product=Product.objects.get(pk =pk)
    except Product.DoesNotExist: 
        return Response("product not found ")
    
    if request.method == 'POST':
        product=Product.objects.prefetch_related('productCategory').get(pk=pk)
        categories = product.productCategory.all()
        try :
            productSerializer= ProductPostSerializer(data=request.data["product"])
            if productSerializer.is_valid (): 
                product.ArabicName = request.data['product']['ArabicName']  
                product.EnglishName= request.data['product']['EnglishName']
                product.code =request.data['product']['code']
                product.image =request.data['product']['image']
                product.save()  
            else:
                return Response (productSerializer.errors)
                    
        except :
            return Response ("invalid input, please enter the product")    
        try:
            for category in request.data["category"]:
                if category["flag"]=="new": 
                  new_category(category=category,product=product)

                elif category["flag"]=="update":
                    demo= update_category(categories=categories,category=category,product=product)
                    if demo:
                        return  update_category(categories=categories,category=category,product=product)
                    else:
                       pass
                elif category["flag"]=="delete":        
                    for category_instance in categories:
                        if category["id"]==category_instance.id:
                            category_instance.delete()
                            flag=0
                            break
                        else:
                            flag=1
                    if flag ==1:
                        return Response("delete category not found")
                   
                      
        except :
            return Response ("invalid input, please enter the category")

        get_product=Product.objects.get(id=product.id)
        categoryProduct=ProductListSerializer(get_product)
        return Response( categoryProduct.data)

def new_category(category,product ):
    categorySerializer = CategorySerializer(data=category)  
    if categorySerializer.is_valid():
            new_category =Category()
            new_category.name = category["name"]
            new_category.description =category["description"]
            new_category.code =category["code"]
            new_category.product =Product.objects.get(id=product.id)
            new_category.save()
    else:
        return Response (categorySerializer.errors)
                
                
def update_category(categories,category,product):
    categorySerializer = CategorySerializer(data=category)
    flag=0
    if categorySerializer.is_valid():
        
        for category_instance in categories:
            
            if category["id"]==category_instance.id:
                
                category_instance.name= category["name"]
                category_instance.description =category["description"]
                category_instance.code =category["code"]
                category_instance.product=Product.objects.get(id=product.id)
                category_instance.save()
                flag=0
                break
            else:
                flag=1
        if flag ==1:
            return Response("update category not found")
    else:
        return Response(categorySerializer.errors)

    



@api_view(['GET'])
def items(request, *args, **kwargs):
    if request.method == 'GET':    
        products= Product.objects.all()
        categoryProduct=ProductListSerializer(products,many =True)
        return Response( categoryProduct.data)  
    
@api_view(['GET'])
def detail_item(request,pk, *args, **kwargs): 
    if request.method == 'GET':    
    
        try :
                
                get_product=Product.objects.get(pk =pk)
                categoryProduct=ProductListSerializer(get_product)
                return Response( categoryProduct.data)  
                
            
        except Product.DoesNotExist:
            return Response("product not found ")  

@api_view(['DELETE'])
def delete_product(request,pk, *args, **kwargs):
    try :
        get_product=Product.objects.get(pk =pk)
        
    except:
        return Response("product not found ")
    
    if request.method == 'DELETE':
        product=Product.objects.prefetch_related('productCategory').get(pk=pk)
        categories = product.productCategory.all()
        
        for category in categories:
            category.delete()

        product.delete()
        return Response("product deleted")

        
@api_view(['DELETE'])
def delete_category(request,pk, *args, **kwargs):
    try :
        get_category=Category.objects.get(pk =pk)
        
    except:
        return Response("category not found ")
    
    if request.method == 'DELETE':
        get_category=Category.objects.get(pk =pk)
        get_category.delete()
        return Response("Category deleted")     
        
        
        

           
        
        
        
        
        


        
          
        

     
   
    

