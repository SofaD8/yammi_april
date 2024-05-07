from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import DishCategory, Dish, EventsCategory, Chefs, Gallery


@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_visible', 'sort', 'slug')
    list_editable = ('name', 'is_visible', 'sort')
    list_filter = ('is_visible',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'price', 'is_visible', 'sort', 'category')
    list_editable = ('price', 'is_visible', 'sort')
    list_filter = ('category', 'is_visible')
    search_fields = ('name',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=50 height=50>')

    photo_src_tag.short_description = 'Dish photo'

    @admin.register(EventsCategory)
    class EventsCategoryAdmin(admin.ModelAdmin):
        list_display = ('id', 'photo_src_tag', 'name','description', 'price', 'is_visible', 'sort',)
        list_editable = ('price', 'is_visible', 'sort')
        list_filter = ('is_visible',)
        search_fields = ('name',)

        def photo_src_tag(self, obj):
            if obj.photo:
                return mark_safe(f'<img src="{obj.photo.url}" width=50 height=50>')

        photo_src_tag.short_description = 'Events photo'

    @admin.register(Chefs)
    class ChefsAdmin(admin.ModelAdmin):
        list_display = ('id', 'photo_src_tag', 'name', 'description', 'sort')
        list_editable = ('description', 'sort')
        search_fields = ('name',)

        def photo_src_tag(self, obj):
            if obj.photo:
                return mark_safe(f'<img src="{obj.photo.url}" width=50 height=50>')

        photo_src_tag.short_description = 'Chefs photo'

    @admin.register(Gallery)
    class GalleryAdmin(admin.ModelAdmin):
        list_display = ('id', 'photo_src_tag', 'sort')
        list_editable = ('sort',)
        search_fields = ('sort',)

        def photo_src_tag(self, obj):
            if obj.photo:
                return mark_safe(f'<img src="{obj.photo.url}" width=50 height=50>')

        photo_src_tag.short_description = 'Photo'