from django.contrib import admin
from .models import Sport


@admin.register(Sport)
class AdminForSport(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    # prepopulated_fields = {
    #     "slug": ("title",),
    # }


# admin.site.register(AnotherModel)
