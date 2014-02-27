from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin
from models import FlipBook,FlipBookPage

class FlipBookPageInline(admin.StackedInline):
    model = FlipBookPage

class FlipBookAdmin(admin.ModelAdmin):
    inlines = [FlipBookPageInline]
    prepopulated_fields = {'slug': ('titulo',)}

admin.site.register(FlipBook, FlipBookAdmin)