from django.contrib import admin
from .models import Project, Enquiry, Socials, Skills, Home
from django.http import HttpResponse
import csv

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'thumbnail', 'webrender', 'is_top']

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['sender_name', 'sender_email', 'purpose', 'subject', 'message']
    actions = ['export_to_csv']

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="enquiries.csv"'
        writer = csv.writer(response)
        writer.writerow(['Sender Name', 'Sender Email', 'Purpose', 'Subject', 'Message'])
        for enquiry in queryset:
            writer.writerow([enquiry.sender_name, enquiry.sender_email, enquiry.purpose, enquiry.subject, enquiry.message])
        return response

    export_to_csv.short_description = 'Export selected enquiries to CSV'

@admin.register(Socials, Skills, Home)
class OtherModelsAdmin(admin.ModelAdmin):
    pass
