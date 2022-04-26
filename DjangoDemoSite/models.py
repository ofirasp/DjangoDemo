from django.db import models

# Create your models here.

class WorkItem:
    count =0
    def __init__(self):
        self.JobId=WorkItem.count
        self.Title = ""
        WorkItem.count+=1

