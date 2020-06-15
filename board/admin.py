from django.contrib import admin
from .models import Board

# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    list_disply = ('title',)


admin.site.register(Board, BoardAdmin)
