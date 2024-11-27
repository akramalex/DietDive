from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Contact


""" Register your models here.
 ContactAdmin customizes the admin interface
  for managing contact form submissions
, allowing easy searching, filtering,
 and rich text editing for the 'message' field."""


@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):

    list_display = ('name', 'email', 'message', 'is_read', 'submitted_on')
    list_filter = ('is_read',)
    search_fields = ('name', 'email', 'message')
    summernote_fields = ('message',)
    list_editable = ('is_read',)
