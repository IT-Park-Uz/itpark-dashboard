from django.contrib import admin
from .models import ItPark

class ItParkAdmin(admin.ModelAdmin):
    list_display = ('admins','filials','startapps','volume','incubation','trained','events','partners','participants','staff') 
    list_editable = ('filials','startapps','volume','incubation','trained','events','partners','participants','staff',)



admin.site.register(ItPark,ItParkAdmin)

