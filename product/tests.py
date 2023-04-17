from django.test import TestCase


# encoded_data = request.data["image"]
      
        
#         #decode base64 string data
#         decoded_data=base64.b64decode(encoded_data)
#         print()
#         print("decoded data")
#         print(decoded_data)
#         print()
#         print()





# Create your tests here.
# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser
# from rest_framework.decorators import parser_classes

# @parser_classes((MultiPartParser, ))
# class UploadFileAndJson(APIView):

#     def post(self, request, format=None):
#         thumbnail = request.FILES["file"]
#         info = json.loads(request.data['info'])
#         ...
#         return HttpResponse()





# # dict_obj = model_to_dict( product )
#         # serialized = json.dumps(product)
#         # print()
#         # print(serialized)
#         # print()
#         serialized_obj = serializers.serialize('json', [ product])
#         serialized = json.dumps(serialized_obj)
#         print("dumps")
#         print(serialized)
#         print()
#         # post_list = serializers.serialize('json', product)
#         print("serializer")
#         print(serialized_obj)
#         print()  
        
#         categoryProduct=ProductListSerializer(serialized)
#         print()
#         print(categoryProduct)
#         print()

        # print (product.code)
        # print (product.code) 
        
#   # serialized_obj = serializers.serialize('json', [ product])
#         # serialized = json.dumps(serialized_obj)
#         print()
#         print(product)
#         print()
#         print()


# category is a variable that is used to represent each individual Category instance in the categories queryset.
# The dictionary is created using a list comprehension, which is a concise way to create a list or other iterable in Python. In this case, the list comprehension is used to create a list of dictionaries, where each dictionary corresponds to an individual Category instance in the categories queryset.

# Here's the list comprehension that creates the category_data list of dictionaries:

# category_data = [{'name': category.name, 'description': category.description} for category in categories]
# category_data = [{'name': category.name, 'description': category.description} for category in categories]

# print()
# print(category_data)
# print()
#output data :
# [{'name': 'mona', 'description': 'mona des'}, {'name': 'hoda', 'description': 'hoda des'}]



# for category in categories:
# print(category.name)
# print()
# print(categories)
# print()


# import base64
# from django.http import JsonResponse
# from myapp.models import MyModel

# def save_base64_image(request):
#     if request.method == 'POST':
#             image_data = request.POST.get('image_data')
#              encoded_image_data = decoded_image_data.encode('utf-8')
# import base64
# from django.http import JsonResponse
# from myapp.models import MyModel





# def save_base64_image(request):
#     if request.method == 'POST':
#         # Get the base64-encoded image data from the request
#         image_data = request.POST.get('image_data')

#         # Decode the base64-encoded image data
#         decoded_image_data = base64.b64decode(image_data)

#         # Encode the decoded image data as a string
#         encoded_image_data = decoded_image_data.encode('utf-8')

#         # Save the encoded image data to the model field
#         my_model = MyModel.objects.get(pk=1) # Replace with your own model instance retrieval
#         my_model.image_field = encoded_image_data
#         my_model.save()

#         # Return a JSON response indicating success
#         return JsonResponse({'success': True})

    # Return a JSON response indicating failure if the request method is not POST
#     return JsonResponse({'success': False, 'error': 'Invalid request method'})
