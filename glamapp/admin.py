from django.contrib import admin
from .models import Categories,Brand,Filter_prize,Product,Images,Contact,Order,Orderitem


class ImagesTabularInline(admin.TabularInline):
    model = Images
class ProductAdmin(admin.ModelAdmin):
    inlines=[ImagesTabularInline]
class OrderitemTabularInline(admin.TabularInline):
    model=Orderitem
class OrderAdmin(admin.ModelAdmin):
     inlines=[OrderitemTabularInline]  
admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Filter_prize)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images)
admin.site.register(Contact)
admin.site.register(Order,OrderAdmin)
admin.site.register(Orderitem)


# Register your models here.



