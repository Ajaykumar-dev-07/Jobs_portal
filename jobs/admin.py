from django.contrib import admin
from .models import UserProfile, Company, JobPost, Application

class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'salary', 'posted_on')
    search_fields = ('title', 'company__name')
    list_filter = ('company',)

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'job', 'applied_on')
    search_fields = ('applicant__user__username', 'job__title')

admin.site.register(UserProfile)
admin.site.register(Company)
admin.site.register(JobPost, JobPostAdmin)
admin.site.register(Application, ApplicationAdmin)
