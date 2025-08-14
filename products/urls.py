from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, share_product

router = DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('share/<int:pk>/', share_product, name='share_product'),
]