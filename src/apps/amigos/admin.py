from django.contrib import admin

from .models import Amigo


# Register your models here.

class AmigosAdmin(admin.ModelAdmin):
	list_display = ['id','nombre','domicilio']


admin.site.register(Amigo, AmigosAdmin)