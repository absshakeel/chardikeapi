
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from orders.database.cart_order import Order

from utils.util import Util


# @receiver(post_save,sender=Order)
# def points_count(sender,instance, created,*args,**kwargs):
#     if created:
#         points_gained = Util.points_calculate(instance.total)

#         try:
#             profile = instance.customer
#             profile.points_gained += points_gained
#             profile.save()

#         except Exception as e:
#             pass



'''
this function for get coupon count and validations check
'''

@receiver(pre_save, sender=Order)
def coupon_count(sender, instance, *args, **kwargs):
    
    try:

        if instance.coupon.coupon_count == instance.coupon.maximum_user:
                instance.coupon.is_active = False
                instance.coupon.save()

        elif instance.coupon is not None:
            instance.coupon.coupon_count += 1
            instance.coupon.save()
        else:
            pass 

    except Exception as e:
        print(e)


'''
Creating auto generated ref code 
'''

import datetime 
# date = datetime.date.today()
# s_date=str(date)

@receiver(post_save,sender=Order)
def Create_ref_code(sender,instance,created,*args,**kwargs):

    if created:
        try:
            instance.ref_code = \
                 f"CH{''.join(e for e in str(datetime.date.today()) if e.isalnum())}{instance.id}" 
            print(instance.ref_code)
            instance.save()
        except Exception as e:
            print(e)


'''
This logic works for order status completed message
'''
from MainApplication.scripts.phone_SMS_settings import SMS_for_Phone_Message

@receiver(post_save,sender=Order)
def Create_ref_code(sender,instance,created,*args,**kwargs):

    if not created and instance.order_status == 'Completed':
        phone = instance.mobile
        message = f"Your payment completed Successfully  at Chardike.com"
        SMS_for_Phone_Message(phone,message).start()
    else:
        pass