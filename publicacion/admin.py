from django.contrib import admin


# Register your models here.
from . import models

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title','id','status','slug','author')
    prepoluted_fields = {'slug': ('title',)}

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','name','email','publish','status')
    list_filter = ('status','publish')
    search_fields = ('name','email','content')


admin.site.register(models.Category)