from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from auth_app.models import Contact,Bmi
admin.site.register(Contact)
class BmiAdmin(admin.ModelAdmin):
    list_display=('user','bmi','weight','height','date')

admin.site.register(Bmi,BmiAdmin)
