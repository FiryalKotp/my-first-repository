from rest_framework import serializers
from product.models import *
import re
class ProductPostSerializer (serializers.Serializer):
    
    ArabicName = serializers.CharField(max_length=80 ,allow_null =False ,allow_blank= False ,required=True)
    EnglishName =serializers.CharField( max_length=80 ,allow_null=False ,allow_blank= False ,required=True )
    code = serializers.CharField( max_length=80 ,allow_null=False ,allow_blank= False ,required=True )     
    
    def validate_EnglishName(self ,value):
        if len(value)<3 :
            raise serializers.ValidationError("the name must be more than three characters")        
        valid_name =re.search(r'^\s?[a-zA-Z\s]+$', value )
        
        
        if valid_name  :
            return value
        else:
             raise serializers.ValidationError("invalid name, please enter character only  ")
    
    
    def validate_ArabicName(self ,value):

        if len(value)<3 :
            
            raise serializers.ValidationError(".عدد الحروف يجب ان يكون اكثر من ثلاثة, من فضلك ادخل اسم مناسب ")
        valid_name= re.match(r'^[\u0621-\u064A\s]+$', value)
        if not valid_name:  
            
             raise serializers.ValidationError("اسم غير صحيح: من فضلك ادخل حروف عربية ومسافات فقط")
        return value
        
 
    

class CategorySerializer (serializers.Serializer):
    name = serializers.CharField(max_length=60 ,allow_null =False,required=True)
    description = serializers.CharField(max_length =200 ,allow_blank =True, allow_null=True,default='description')
    code = serializers.CharField( max_length=80 ,allow_null=False ,allow_blank= False  ) 
    
    
    def validate_name(self ,value):
        if len(value)<3 :
            raise serializers.ValidationError("the name must be more than three characters")
        
        valid_name =re.search(r'^\s?[a-zA-Z\s]+$', value )
        if valid_name  : 
            return value
        else:
             raise serializers.ValidationError("invalid name, please enter character only.  ")
    
class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = ['id','name', 'description','code','product' ]    
        
class ProductListSerializer(serializers.ModelSerializer):
    productCategory=CategoryListSerializer(many=True)
    class Meta:
        model=Product
        fields = ['id','ArabicName','EnglishName','code','image','productCategory']
        
        

