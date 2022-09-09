from django.contrib import admin

from .models import IdeaModel


class IdeaAdmin(admin.ModelAdmin):
    """Настройки админки."""
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'scale',
        'coordinate_x',
        'coordinate_y'
    )

    list_editable = ('scale',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(IdeaModel, IdeaAdmin)
