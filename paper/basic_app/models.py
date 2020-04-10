from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.
class Exam(models.Model):
    BRANCH=[('CS','CS'),('ME','ME'),('PIE','PIE'),('EE','EE'),('CE','CE'),('ECE','ECE')]
    SEM=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8)]
    SESSIONAL=[('MidSem 1','MidSem 1'),('MidSem 2','MidSem 2'),('EndSem','EndSem')]
    YEAR=[('2020','2020'),('2019','2019'),('2018','2018'),('2017','2017'),('2016','2016')]

    name=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    branch=models.CharField(max_length=200,choices=BRANCH)
    semester=models.PositiveIntegerField(choices=SEM)
    file=models.FileField(null=True)
    published_date=models.DateTimeField(blank=True,null=True)
    sessional=models.CharField(max_length=200,choices=SESSIONAL,null=True)
    year=models.CharField(max_length=200,choices=YEAR,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('exam_list')

    def __str__(self):
        return self.branch
