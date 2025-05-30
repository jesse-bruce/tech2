from django.shortcuts import render
from.models import Product
# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def products(request):
    products = Product.objects.all()

    context = {
    'products' : products, 
}
    return render(request, 'home/products.html', context)

    
    
    
 
    

    