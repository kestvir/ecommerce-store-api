from django.contrib import admin

from .models import *

admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)
admin.site.register(Payment)
