from django.contrib import admin

# Register your models here.
from webapp.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'project']
    list_display_links = ['id', 'project']
    list_filter = ['project']
    search_fields = ['project', 'status']
    fields = ['project', 'status', 'some_date']


admin.site.register(Article, ArticleAdmin)