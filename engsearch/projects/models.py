from django.db import models
from django.db.models import JSONField

# Create your models here.
class CollegeDB(models.Model): 
     clgname = models.CharField(max_length=100)
     def __str__(self) -> str:
          return self.clgname


class BranchDB(models.Model):
     brname = models.CharField(max_length=50)
     def __str__(self) -> str:
          return self.brname


class SeatMetrixDb(models.Model):
     #name = models.CharField(max_length=500)
     #cutoff = models.IntegerField(default=-1)
     info = JSONField(default=dict)
     #branch = models.ForeignKey(BranchDB, on_delete=models.PROTECT)
     #cutoff = models.IntegerField(default=0)