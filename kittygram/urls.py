from django.urls import include, path
from rest_framework.routers import SimpleRouter

from cats import views

# Для дженериков.
# urlpatterns = [
#     path('cats/', views.CatList.as_view()),
#     path('cats/<int:pk>/', views.CatDetail.as_view()),
# ]


# Роутеры.
router = SimpleRouter()
router.register('cats', views.CatViewSer, basename='tiger')

urlpatterns = [
    path('', include(router.urls)),
]
