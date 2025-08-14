from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def products_page(request):
    return render(request, "products.html")

def register_page(request):
    return render(request, "register.html")

def login_page(request):
    return render(request, "login.html")

def profile_page(request):
    return render(request, "profile.html")

def upload_product_page(request):
    return render(request, "upload_product.html")

def edit_profile_page(request):
    return render(request, "edit_profile.html")

def cart_page(request):
    return render(request, "cart.html")





