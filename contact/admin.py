from django.contrib import admin
from .models import Contact
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):

    list_display = ('name', 'email', 'message', 'is_read', 'submitted_on')  # Columns to display in the list view
    list_filter = ('is_read',)  # Adds a filter for "is_read" status
    search_fields = ('name', 'email', 'message')  # Enables search by name, email, and message
    summernote_fields = ('message',)  # Enables rich text editing for the message field

    # Optionally, make 'is_read' clickable to mark it as read/unread directly
    list_editable = ('is_read',)  # Makes 'is_read' editable directly from the list view