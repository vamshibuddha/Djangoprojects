from django.contrib import admin
from jobs.models import nl_jobs

class jobsAdmin(admin.ModelAdmin):
    list_display = ['job_no', 'job_des', 'job_loc', 'job_skill', 'job_sal', 'job_stdt']
# Register your models here.
admin.site.register(nl_jobs, jobsAdmin)

