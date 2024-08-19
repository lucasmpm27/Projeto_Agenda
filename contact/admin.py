from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name','last_name','phone','show',
    ordering = 'id',
   # list_filter = 'created_date' #listar por data
    search_fields = 'id','first_name','last_name', #cria uma pesquisa
    list_per_page = 10 #lista por página
    list_max_show_all=200 #máximo por lista
    list_editable = 'first_name','last_name','show',
    list_display_links = 'id','phone', #lista de links para acessar cadastro

# Register your models here.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',

