from django.contrib import admin
from .models import Human, Profession


# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'weight', 'birthday', 'is_live')
    list_display_links = ('name', 'age')
    search_fields = ['name']


class ProfessionAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


admin.site.register(Human, RegisterAdmin)
admin.site.register(Profession, ProfessionAdmin)