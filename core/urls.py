from django.urls import path
from .views import index, products_page, register_page, login_page, profile_page, upload_product_page, edit_profile_page, cart_page

urlpatterns = [
    path('', index, name='home'),
    path('products/', products_page, name='products'),
    path('register/', register_page, name='register'),  # ✅ fix here
    path('login/', login_page, name='login'),            # ✅ fix here
    path('profile/', profile_page, name='profile'),
    path('upload/', upload_product_page, name='upload_product'),
    path('profile/edit/', edit_profile_page, name='edit_profile'),
    path('cart/', cart_page, name='cart'),

    # path('products/<int:product_id>/', product_detail_page, name='product_detail'),  # ✅ fix here
    # path('products/<int:product_id>/edit/', edit_product_page, name='edit_product'),
    # path('products/<int:product_id>/delete/', delete_product_page, name='delete_product'),

]


