from django.contrib import admin
from .models import JobApplication


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('company', 'job_title', 'recruiter', 'date_applied', 'rejected', 'ghosted')
    ordering = ('-ghosted', '-rejected', '-date_applied', 'company')
