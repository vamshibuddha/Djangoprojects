from django.db import models

# Create your models here.
class nl_jobs(models.Model):
    job_no = models.IntegerField()
    job_des = models.CharField(max_length=20)
    job_loc = models.CharField(max_length=20)
    job_skill = models.CharField(max_length=50)
    job_sal = models.FloatField()
    job_stdt = models.DateField()
