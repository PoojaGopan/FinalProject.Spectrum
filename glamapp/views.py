from django.shortcuts import render,redirect
from django.http import HttpResponse
from glamapp.models import Product
from glamapp.models import Categories,Filter_prize,Brand,Contact,Order,Orderitem
import razorpay
from django.conf import settings
client=razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
# def my_view(request):
#     return HttpResponse('hi')


#base.html
def base(request):
    return render(request,'base.html')
#index.html
def index(request):
    product=Product.objects.filter(status='publish')
    context={'product':product,
             }
    return render(request,'index.html',context)
#product.html
def product(request):
    product=Product.objects.filter(status='publish')
    categories=Categories.objects.all()
    filterprize=Filter_prize.objects.all()
    brand=Brand.objects.all()
    #id
    CATID=request.GET.get('categories')
    prize_filter_id=request.GET.get('filter_price')
    brand_id=request.GET.get('brand')
    if CATID:
        product=Product.objects.filter(categories=CATID)
    elif prize_filter_id:
        product=Product.objects.filter(filter_price=prize_filter_id)
    elif brand_id:
        product=Product.objects.filter(brand=brand_id)
    else:
         product=Product.objects.filter(status='publish')
   

    context={
        'product':product,
        'categories':categories,
        'filterprize':filterprize,
        'brand':brand,
             }
    return render(request,'product.html',context)
#search.html
def search(request):
    # Get the search query from the GET parameters
    query = request.GET.get('query', '')
    # Filter products based on a case-insensitive partial match on the 'name' field
    product = Product.objects.filter(name__icontains=query)
    # Prepare the context to be passed to the template
    context = {
        'query': query,
        'product': product,
    }
    # Render the search results using the 'search.html' template
    return render(request, 'search.html', context)
#single product.html

def singleproduct(request,id):
    #FILTER WITH ID
    prod=Product.objects.filter(id=id).first()
    context={
        'prod':prod
    }
    return render(request, 'productsingle.html',context)
#contact.html
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
      
        email=request.POST.get('email')
      
        subject=request.POST.get('subject')
      
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
        return redirect('index')
    return render(request,'contact.html')
#login.html

from django.contrib.auth import authenticate,login as auth_login
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            auth_login(request, user)  # Use the correct function name and pass the user object
            return redirect('index')
        else:
            # Handle the case where authentication fails
            return redirect('login')
    return render(request,'login.html')

from django.contrib.auth.models import User
#registration.html
def registration(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        customer = User.objects.create_user(username, email, pass1)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.save()
        return redirect('login')
    return render(request,'registration.html')

#logout
from django.contrib.auth import logout as auth_logout
def logout(request):
    auth_logout(request)
    return redirect('/')






#card details
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_detail(request):
    # product=Product.objects.all()
    # context = {
        
    #     'product': product,
    # }
    return render(request, 'cartdetails.html')

def checkout(request):
    payment=client.order.create({'amount':500,'currency':'INR','payment_capture':'1'})
 
    order_id=payment['id']
    context={
        'order_id':order_id,
        'payment':payment,

    }
    return render(request,'checkout.html',context)

def placeout(request):
    if request.method =='POST':
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(id=uid)
        cart=request.session.get('cart')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        country=request.POST.get('country')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        postcode=request.POST.get('postcode')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        amount=request.POST.get('amount')
       

        order_id=request.POST.get('order_id')
        payment=request.POST.get('payment')

        order=Order(user=user,firstname=firstname,lastname=lastname,
                    country=country,address=address,city=city,state=state,postcode=postcode,
                    email=email,phone=phone,payment_id=order_id,amount=amount)
        order.save()
        for i in cart:
            any=int(cart[i]['price'])
            another=int(cart[i]['quantity'])
            total=any*another
            item=Orderitem(order=order,
                           product=cart[i]['name'],
                           image=cart[i]['image'],
                           quantity=cart[i]['quantity'],
                           price=cart[i]['price'],
                           total=total
                           )
            item.save()
    return render(request,'placeout.html')






def receipt(request):
    totalAmount = calculateTotalAmount(request)  # Pass the request object to the function
    response = get_payment_response()  # Implement this function to get the Razorpay payment response

    context = {
        'totalAmount': totalAmount,
        'response': response,
    }

    return render(request, 'receipt.html', context)


def calculateTotalAmount(request):
    # Ensure that the quantities and prices are converted to integers before performing calculations
    totalAmount = 0
    for key, value in request.session.get('cart', {}).items():
        totalAmount += int(value['price']) * int(value['quantity'])
    return totalAmount

def get_payment_response():
    # Implement your logic to get the Razorpay payment response
    # This can include fetching data from the payment gateway or any other source
    # For demonstration purposes, a dummy response is returned
    return {
        'razorpay_payment_id': 'rzp_test_bdhXja6YIYa195',
        'razorpay_order_id': '5Saohy8E0RUb5WqdVpE7iUEc',
        
    }

