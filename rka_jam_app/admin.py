from django.contrib import admin
from .models import JobApplication


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('company', 'job_title', 'date_applied', 'rejected')
    ordering = ('-rejected', '-date_applied')
