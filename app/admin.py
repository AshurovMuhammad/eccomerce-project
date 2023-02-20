from django.contrib import admin
from .models import Product, Customer, Cart, Payment, OrderPlaced, Wishlist
from django.contrib.auth.models import Group


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
     list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']
     list_display_links = ('title',)


@admin.register(Customer)
class CostumerModelAdmin(admin.ModelAdmin):
     list_display = ['id', 'user', 'locality', 'city', 'state', 'mobile', 'zipcode']
     list_display_links = ('user',)


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
     list_display = ['id', 'user', 'product', 'quantity']
     list_display_links = ('user',)


@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
     list_display = ['id', 'user', 'amount', 'razorpay_order_id', 'razorpay_payment_status', 'razorpay_payment_id', 'paid']
     list_display_links = ('user',)


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
     list_display = ['id', 'user', 'customer', 'product', 'quantity', 'ordered_date', 'status', 'payment']
     list_display_links = ('user',)


@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
     list_display = ['id', 'user', 'product']
     list_display_links = ('user',)


admin.site.site_header = 'Muhammad Dairy'
admin.site.site_title = 'Muhammad Dairy'
admin.site.site_index_title = 'Welcome to Muhammad Dairy Shop'
admin.site.unregister(Group)