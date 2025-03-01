from django.contrib import admin
from .models import *


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ['phone', 'email']
    fields = [
        'phone',
        'email',
        'facebook_url',
        'twitter_url',
        'linkedin_url',
        'instagram_url',
        'signup_url',
    ]

class FooterLinkInline(admin.TabularInline):
    model = FooterLink
    extra = 1
    fields = ['title', 'url', 'order']
@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ['phone', 'address']
    inlines = [FooterLinkInline]
    fieldsets = (
        ('Newsletter Section', {
            'fields': ('newsletter_title', 'newsletter_description')
        }),
        ('Contact Info', {
            'fields': ('address', 'phone', 'map_link')
        }),
        ('Copyright Section', {
            'fields': ('copyright_text', 'design_credit')
        }),
    )