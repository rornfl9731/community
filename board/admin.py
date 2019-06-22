from django.contrib import admin
from board.models import Board,Comment

# Register your models here.

admin.site.register(Comment)


from django_summernote.admin import SummernoteModelAdmin
from .models import Board

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    list_display = ('title', 'writer', 'registered_dttm')
    summernote_fields = '__all__'

admin.site.register(Board, SomeModelAdmin)