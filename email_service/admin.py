from django.contrib import admin
from .models import EmailLog, SenderEmail


class SenderEmailAdmin(admin.ModelAdmin):
    list_display = ('email_address', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('email_address',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Email Credentials', {
            'fields': ('email_address', 'password', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


admin.site.register(EmailLog)
admin.site.register(SenderEmail, SenderEmailAdmin)