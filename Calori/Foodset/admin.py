from django.contrib import admin
from .models import *


class foodAdmin(admin.ModelAdmin):
    class Meta:
        model=FoodItems
        list_display=['name']
        list_filter=['name']


admin.site.register(Customer)
admin.site.register(UserFoodItem)
admin.site.register(Category)
admin.site.register(FoodItems,foodAdmin)
