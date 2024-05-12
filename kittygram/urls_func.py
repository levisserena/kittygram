from django.urls import path

from kittygram.cats import views_func

urlpatterns = [
   path('cats/', views_func.cat_list),
   path('cats/<int:pk>/', views_func.api_cat_detail),
]
