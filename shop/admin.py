from django.contrib import admin

from shop.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "deactivated")
    list_filter = ("deactivated",)
    search_fields = ("name", "price")
    ordering = ("-price",)

    def make_deactivated(self, request, queryset):
        queryset.update(deactivated=True)

    make_deactivated.short_description = "غیرفعال کردن محصولات"

    actions = (make_deactivated,)


class ProductInstanceAdmin(admin.ModelAdmin):
    list_display = ("product",)


admin.site.register(Member)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductInstance, ProductInstanceAdmin)
