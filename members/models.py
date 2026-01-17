from django.db import models
from django.contrib.auth.models import user

class tasks(models.Model):
    user = models.ForeignKey(user, related_name='tasks')
    task = models.CharField(max_length=35)
    desc = models.TextField()
    priority_choice = [('H','High'),('M','Medium'),('L','Low')]
    priority = models.CharField(max_length=1,choices=priority_choice)
    status_choices = [('P','Pending'),('I','In-Progress'),('C','Completed')]
    status = models.CharField(max_length=1,choices=status_choices)
    created_t = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True,blank=True)
    update_t = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name