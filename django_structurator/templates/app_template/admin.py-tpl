"""
@admin.register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    list_display = ("field1", "field2", "created_at")
    list_editable = ("status",)
    readonly_fields = ("created_at", "updated_at")
    list_filter = ("status", "created_at")
    search_fields = ("field1", "field3")
    prepopulated_fields = {"slug_field": ("title_field",)}
    ordering = ("-created_at",)
    list_per_page = 20
    fieldsets = (
        (
            None,
            {
                "fields": ("field1", "field2"),
            },
        ),
        (
            'Advanced options',
            {
                "classes": ("collapse",),  # Collapsible section
                "fields": ("field3", "field4"),
            },
        ),
    )
    inlines = [
        # ExampleInlineAdmin,
    ]

class ExampleInlineAdmin(admin.TabularInline):  #or admin.StackedInline
    model = RelatedModel
    extra = 1
    fields = ("field1", "field2")
"""
from django.contrib import admin
from .models import *
# Register your models here.

