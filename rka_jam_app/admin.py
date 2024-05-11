from django.contrib import admin
from django.db.models import Q
from .models import JobApplication


class IsActiveFilter(admin.SimpleListFilter):
    title = 'Is active?'
    parameter_name = 'is_active'

    def lookups(self, request, model_admin):
        return [
            ('true', 'Yes'),
            ('false', 'No'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'true':
            return queryset.filter(
                rejected=False,
                ghosted=False,
                not_proceeding=False
            )

        if self.value() == 'false':
            return queryset.filter(
                Q(rejected=True) | Q(ghosted=True) | Q(not_proceeding=True)
            )


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('company', 'job_title', 'recruiter', 'date_applied', 'rejected', 'ghosted', 'not_proceeding')
    ordering = ('ghosted', 'rejected', 'not_proceeding', '-date_applied', 'company')
    list_filter = [IsActiveFilter]
