from django.contrib import admin
from .models import New,Contact,Comment


@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title","category","status","published_at")
    list_filter = ("status","category")
    search_fields = ("title","body")
    prepopulated_fields = {"slug":("title",)}



admin.site.register(Contact)
admin.site.register(Comment)
