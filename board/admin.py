from django.contrib import admin
from board.models import Board,Comment

# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title','writer','registered_dttm')

admin.site.register(Board,BoardAdmin)
admin.site.register(Comment)