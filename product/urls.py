from django.urls import path 
from . import views 


urlpatterns = [
path("new_item",views.new_item, name="new_item"),
path("detail_item/<int:pk>",views.detail_item, name="detail_item"),
path("update_item/<int:pk>",views.update_item, name="update_item"),
path("delete_product/<int:pk>",views.delete_product, name="delete_product"),
path("delete_category/<int:pk>",views.delete_category, name="delete_category"),
path("items",views.items, name="items"),
]
