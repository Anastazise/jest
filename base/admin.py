from django.contrib import admin

# Register your models here.

from .models import Room, Message, Carousel, Product, Pool

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Carousel)
admin.site.register(Product)
admin.site.register(Pool)

