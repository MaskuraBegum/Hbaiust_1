from django.db import models

# Create your models here.
class CoverPage(models.Model):
    uniName = models.CharField( max_length=200)
    sname = models.CharField( max_length=50)
    sid = models.IntegerField()
    session = models.CharField(max_length=50, default="DefaultSession")
    coruse_code = models.TextField()

    def __str__(self):
        return self.name