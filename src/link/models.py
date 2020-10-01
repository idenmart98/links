from django.db import models

# Create your models here.


class Links(models.Model):
    old_link = models.CharField(max_length=500)
    new_link = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)