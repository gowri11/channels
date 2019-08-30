from django.contrib import admin
from .models import Register
from .models import Dishes

class Chaitu(admin.ModelAdmin):
    list_display=['name','area','email','mobile','city']
admin.site.register(Register,Chaitu)

class gowri(admin.ModelAdmin):
    list_display=['viewer_name','mobile','email','amount','recharge_date','expire_date','MY_CHOICES']
admin.site.register(Dishes,gowri)

# Register your models here.
# class bujji(admin.ModelAdmin):
#     list_display=[]