from django.db import models

# Create your models here.
JOB_TYPE = (
    ('first_time','first_time'),
    ('part_time','part_time')
)
class Job(models.Model):
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=15,choices=JOB_TYPE,default='')
    description = models.TextField(max_length=1000,default='')
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    #category
    experience = models.IntegerField(default=1)




    def __str__(self):
        return self.title