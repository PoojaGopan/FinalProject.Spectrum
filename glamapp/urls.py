from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('base/',views.base,name='base'),
    path('product/',views.product,name='product'),
    path('search/',views.search,name='search'),
    path('<int:id>/', views.singleproduct, name='singleproduct'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('registration/',views.registration,name='registration'),
    path('logout/',views.logout,name='logout'),
    #cart session
    # path('cartdetails/',views.cartdetails,name='cartdetails'),



    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('checkout/',views.checkout, name='checkout'),

    path('placeout/', views.placeout, name='placeout'),

    path('receipt/',views.receipt,name='receipt')
]