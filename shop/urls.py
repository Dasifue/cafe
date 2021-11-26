from .views import all_products, products_filter, saveorder
from django.urls import path

app_name = 'shop'

urlpatterns = [
    path("all_p", all_products, name = 'all_products'),
    path("products_filter/<int:category_id>", products_filter, name = 'products_filter'),
    path("saveorder", saveorder, name='saveorder')
]