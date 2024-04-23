from django.db import models
from django.utils import timezone


class JobApplication(models.Model):
    company = models.CharField(max_length=100, help_text='Company that is presenting the opportunity')
    job_title = models.CharField(max_length=100, help_text='Job title')
    job_url = models.URLField(null=True, blank=True, help_text='The url for the job ad')
    recruiter = models.CharField(null=True, max_length=100, help_text='Recruiter name')
    recruiter_contacts = models.TextField(null=True, blank=True, help_text='Recruiter contacts')
    job_description = models.TextField(help_text='The job description')
    date_applied = models.DateField(default=timezone.now, help_text='The date I applied')
    notes = models.TextField(null=True, blank=True, help_text='Any notes relevant to the process')
    rejected = models.BooleanField(default=False, help_text='If I was rejected in this process')
    ghosted = models.BooleanField(default=False, help_text='If I was ghosted in this process')
    not_proceeding = models.BooleanField(default=False, help_text="If I didn't want to proceed in the process")

    def __str__(self):
        return f'{self.job_title} ({self.company})'
