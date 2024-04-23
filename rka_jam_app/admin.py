from django.contrib import admin
from .models import JobApplication


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('company', 'job_title', 'recruiter', 'date_applied', 'rejected', 'ghosted', 'not_proceeding')
    ordering = ('ghosted', 'rejected', 'not_proceeding', '-date_applied', 'company')
