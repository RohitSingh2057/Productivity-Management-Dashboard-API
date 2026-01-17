from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, related_name='tasks',on_delete=models.CASCADE)
    title = models.CharField(max_length=35)
    desc = models.TextField()
    priority_choice = [('H','High'),('M','Medium'),('L','Low')]
    priority = models.CharField(max_length=1,choices=priority_choice)
    status_choices = [('P','Pending'),('I','In-Progress'),('C','Completed')]
    status = models.CharField(max_length=1,choices=status_choices)
    created_t = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True,blank=True)
    update_t = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task