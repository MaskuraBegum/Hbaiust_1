from django.db import models

# Create your models here.
class Cover_page(models.Model):
    uniName = models.CharField( max_length=50)
    name = models.CharField( max_length=50)
    id = models.IntegerField()
    coruseName = models.TextField()

    def __str__(self):
        return self.name
    
