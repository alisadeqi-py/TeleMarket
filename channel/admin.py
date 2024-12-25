from django.contrib import admin
from .models import Channel, Post

class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'is_free', 'price', 'created_at', 'new_message_timestamp')
    list_filter = ('is_free', 'created_at', 'new_message_timestamp')
    search_fields = ('name', 'description', 'creator__username', 'creator__email')
    ordering = ('created_at',)
    readonly_fields = ('id',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('channel', 'created_by', 'created_at', 'scheduled_at', 'is_deleted')
    list_filter = ('is_deleted', 'created_at', 'scheduled_at')
    search_fields = ('content', 'channel__name', 'created_by__username', 'created_by__email')
    ordering = ('created_at',)
    readonly_fields = ('id',)

# Registering the models and admin classes
admin.site.register(Channel, ChannelAdmin)
admin.site.register(Post, PostAdmin)
