from django.shortcuts import render
from jobs.models import nl_jobs
# Create your views here.
def nljobs(request):
    job_list = nl_jobs.objects.all()
    my_dict = {'job_list': job_list}
    return render(request, 'jobs/jobs.html', context=my_dict)
