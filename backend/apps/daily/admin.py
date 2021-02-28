from django.contrib import admin
from .models import Daily

class DailyAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at', 
        'modified'
    )
    list_display = (
        'title', 
        'description', 
        'completed'
    )
    


admin.site.register(Daily, DailyAdmin)