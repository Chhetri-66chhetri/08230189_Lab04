from django.contrib import admin
from .models import Journey

@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'start_date')
    search_fields = ('title', 'description', 'created_by__username')
