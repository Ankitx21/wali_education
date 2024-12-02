from django.contrib import admin
from wali_institute.models import AdmissionEnquiry

@admin.register(AdmissionEnquiry)
class AdmissionEnquiryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'subject', 'email', 'mobile', 'created_at')
    list_filter = ('subject', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'mobile')
    ordering = ('-created_at',)