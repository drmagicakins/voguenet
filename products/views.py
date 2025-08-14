from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Product, Like, Comment
from .serializers import (
    ProductSerializer,
    LikeSerializer,
    CommentSerializer,
)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("-created")
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        product = self.get_object()
        like, created = Like.objects.get_or_create(user=request.user, product=product)
        if not created:
            like.delete()
            return Response({"liked": False})
        return Response({"liked": True})

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def comment(self, request, pk=None):
        product = self.get_object()
        comment = Comment.objects.create(
            user=request.user,
            product=product,
            text=request.data.get("text", ""),
        )
        return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)


# ---------- standalone helper view ----------
def share_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    url = request.build_absolute_uri(f"/products/{pk}/")
    return JsonResponse({
        "facebook": f"https://facebook.com/sharer/sharer.php?u={url}",
        "twitter":  f"https://twitter.com/intent/tweet?url={url}&text={product.name}",
    })
# This view allows sharing a product via social media links.