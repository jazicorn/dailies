from django.contrib import admin
from .models import Daily

class DailyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
    readonly_fields = ('created', 'modified')
# Register your models here.

admin.site.register(Daily, DailyAdmin)