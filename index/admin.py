from django.contrib import admin
from .models import Section, Category, PhotoAlbum, Photo


@admin.register(Section)
class SectionModelAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'order',
    )

    list_editable = ('order',)


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'section',
    )

    list_filter = (
        'section',
    )


class PhotoModelAdmin(admin.TabularInline):
    model = Photo


@admin.register(PhotoAlbum)
class PhotoAlbumModelAdmin(admin.ModelAdmin):
    list_display = ('title', )
    inlines = (
        PhotoModelAdmin,
    )
