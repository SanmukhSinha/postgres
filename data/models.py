from django.db import models
from django.utils import timezone

class Data(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    comment = models.TextField()
    date = models.DateTimeField(blank=True, null=True)

    def store(self):
        self.date = timezone.now()
        self.save()

    class Meta:
        verbose_name = ('Comment')

    def __str__(self):
        return (self.first_name + ' ' +self.last_name)  
