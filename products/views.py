from django.http import JsonResponse
from django.shortcuts import render, redirect
from . models import ProductItem, Brand, Category, Size
from django.template.loader import render_to_string



# Create your views here.
def index(request):
    try:
        # Get the brand named "Nike"
        # nike_brand = Brand.objects.get(brand_name__iexact='nike')

        # Get the last added product for the "Nike" brand
        last_added_product = ProductItem.objects.filter(brand_id__brand_name__iexact='nike').latest('id')

    except Brand.DoesNotExist:
        # Handle the case if the brand "Nike" does not exist
        last_added_product = None

    products = ProductItem.objects.order_by('-createdDate')[:8]

    categories = Category.objects.all()
    #do it in cache

    # Category = Category.objects.all()


    context = {
        'last_added_product': last_added_product,
        'products': products,
        'categories': categories
    }

    return render(request, "index.html", context)

def productList(request):

    #try to add select to fetch data from other tables(foriegn key)
    products = ProductItem.objects.all()

    # colors = ProductItem.objects.values_list('color_id__color_value', flat=True).distinct()

    # brand = ProductItem.objects.values_list('brand_id__brand_name', flat=True).distinct()

    # category = ProductItem.objects.values_list('category_id__name', flat=True).distinct()


    context = {
        'products': products,
    }
    return render(request, "category.html", context)

def productDetail(request, id):

#can use prefetch related in case of images
    products = ProductItem.objects.get(id=id)

    sizes = Size.objects.all()

    p_image = products.p_images.all()

    context = {
        'products': products,
        'p_image': p_image,
        'sizes': sizes
    }

    return render(request, "single-product.html", context)


def filter_product(request):
    categories = request.GET.getlist('category[]')
    brands     = request.GET.getlist('brand[]')
    colors     = request.GET.getlist('color[]')

    min_price = request.GET['min_price']
    max_price = request.GET['max_price']

    products   = ProductItem.objects.order_by("-id").distinct()

    # Apply price range filtering
    products = products.filter(price__gte=min_price, price__lte=max_price) #lte = less than or equal to

    if len(categories) > 0:
        products = products.filter(category_id__id__in = categories).distinct()

    if len(brands) > 0:
        products = products.filter(brand_id__id__in = brands).distinct()

    if len(colors) > 0:
        products = products.filter(color_id__id__in = colors).distinct()

    data = render_to_string("ajax/product-list.html", {'products': products})

    return JsonResponse({"data": data})