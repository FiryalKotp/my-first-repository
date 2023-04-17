from django.db import models

# Create your models here.
class Product(models.Model):
    ArabicName = models.CharField(max_length=80 ,null =False ,blank= False)
    EnglishName =models.CharField( max_length=80 ,null=False ,blank= False  )
    code = models.CharField( max_length=80 ,null=False ,blank= False  ) 
    image = models.FileField( upload_to="photo/%y/%m/%d",null=True,blank=True)
    
    
class Category(models.Model):
    name =models.CharField(max_length=50 ,null =False ,default='name')
    description = models.TextField(max_length =200 ,blank =True, null=True,default='description')
    code = models.CharField( max_length=80 ,null=False ,blank= False  ) 
    product = models.ForeignKey(Product,on_delete=models.PROTECT,related_name='productCategory')