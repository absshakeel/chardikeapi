from accounts.models.initials import InitModels
from django.conf import settings
from django.db import models
from products.database.products import Products


class Cart(InitModels):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    total = models.PositiveIntegerField()
    complete = models.BooleanField(default=False)

class CartProduct(InitModels):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ManyToManyField(Products)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Cart=={self.cart.id}<==>CartProduct:{self.id}==Qualtity=={self.quantity}"


ORDER_STATUS = (
    ("Pending","Pending"),
    ("Confirmed", "Confirmed"),
    ("Shipped", "Shipped"),

    ("On Hold", "On Hold"),
    ("Completed","Completed"),
    ("Canceled", "Canceled"),
    
    ("Refunded", "Refunded"),
    ("Failed", "Failed"),
    ("Deleted", "Deleted"),   
)

ORDER_PAY_METHOD = (
    ("Cash on Delivery", "Cash on Delivery"),
    ("SSL Commerz", "SSL Commerz"),
)

DELIVERY_OPTIONS = (
    ('Dhaka Fast Delivery','Dhaka Fast Delivery'),
    ('Dhaka Slow Delivery','Dhaka Slow Delivery'),
    ('Cash On Delivery', 'Cash On Delivery'),
    ('Sundarban', 'Sundarban'),
)



'''
Cart & Order Management
    - Order models
    - Cart models
    - Cart Item models
'''


## Order Item Models 
class OrderItem(InitModels):
    # customer = models.ForeignKey('accounts.Profile',on_delete=models.CASCADE,
    #     null=True,verbose_name="Customer Name",related_name="order_items")
    item = models.ForeignKey('products.Products',
        on_delete=models.SET_NULL,
        null=True,verbose_name="Products",
        related_name="items"
    )
    quantity = models.IntegerField(null=True,verbose_name="Quantity")
    attr = models.CharField(max_length=300,null=True,blank=True,verbose_name="Attribute")
    is_order = models.BooleanField(default=False) 
    amount_item = models.PositiveIntegerField(null=True,verbose_name="Unit Price")
    total_amount_item = models.PositiveBigIntegerField(
        null=True,
        verbose_name="Total Unit Price",
        blank=True
    )
    
    def __str__(self):
        return f"Item : {self.item} === Quantitiy  \
                : {self.quantity} === Status : {'Paid' if self.is_order == True else 'Not paid'}"

    class Meta:
        verbose_name_plural =  "Order Item"


class Order(InitModels):
    # cart  = models.OneToOneField(Cart,on_delete=models.CASCADE)
    customer = models.ForeignKey('accounts.Profile',on_delete=models.SET_NULL,null=True,
        verbose_name="Customer",related_name="orders")

    ref_code = models.CharField(max_length=255, null=True,blank=True, unique=True)

    mobile = models.CharField(max_length=16,null=True,blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)

    address_shipping = models.ForeignKey('accounts.BillingAddress',on_delete=models.SET_NULL,
        null=True,blank=True, related_name='shiping_address')
    
    address_billing = models.ForeignKey('accounts.BillingAddress', on_delete=models.SET_NULL, 
    null=True,blank=True,related_name='billing_address')

    coupon = models.ForeignKey('orders.Coupon',blank=True,null=True,
        on_delete=models.SET_NULL)
    ordered_date = models.DateTimeField(null=True)
    items = models.ManyToManyField(OrderItem,related_name='items')

    # shippng fee, discount fix price 
    shipping_fee = models.PositiveIntegerField(default=0)
    discount_price = models.PositiveIntegerField(default=0)
    
    subtotal =models.PositiveIntegerField(default=0)

    total = models.PositiveIntegerField()
    # discount = models.PositiveIntegerField()

    order_status = models.CharField(max_length=100,choices=ORDER_STATUS,
        default="Pending")

    fast_delivery = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=100,choices=ORDER_PAY_METHOD,
        default="Cash on Delivery")

    payment_complete = models.BooleanField(default=False)
    is_order = models.BooleanField(default=False,null=True)
    
    # new add delivery options   
    delivery_option = models.CharField(max_length=255,choices=DELIVERY_OPTIONS,
        default="Cash On Delivery")

    # order from 
    order_from = models.CharField(max_length=255,null=True, blank=True)
    
    user_device = models.CharField(max_length=255, null=True,blank=True)
    user_browser = models.CharField(max_length=255, null=True,blank=True)

    def __str__(self):
        return str(self.customer)

    class Meta:
        verbose_name_plural = 'Customer Order'
    
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         if self.total <= 1000:
    #             points_gained = 0.1 * self.total
    #         elif self.total >1000 and self.total <= 3000:
    #             points_gained = 0.3 * self.total
    #         elif self.total >3000 and self.total <= 5000:
    #             points_gained = 0.5 * self.total
    #         elif self.total >5000 and self.total <= 10000:
    #             points_gained = 0.7 * self.total
    #         else:
    #             points_gained = 0.8 * self.total
        
    #         try:
    #             profile = self.customer
    #             print(profile)
    #             profile.points_gained += points_gained
                
    #             profile.save()

    #         except Exception as e:
    #             print(e)

    #     super().save(*args, **kwargs)


    # custom property 
    # @property
    # def coupon_count(self):
    #     c_count = 0
    #     if self.coupon is not None:
    #         c_count += 1
    #         return c_count
    #     else:
    #         return c_count 


'''
shipping address foreingkey need
'''