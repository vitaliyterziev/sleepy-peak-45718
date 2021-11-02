from django.contrib import admin
from .models import Entry, Comment

# Register your models here.


class EntryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Entry, EntryAdmin)
admin.site.register(Comment)
