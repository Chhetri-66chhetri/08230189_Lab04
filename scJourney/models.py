from django.db import models
from django.contrib.auth.models import User

class Journey(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('PL', 'Planned'),
        ('IP', 'In Progress'),
        ('CM', 'Completed'),
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='PL')

    def __str__(self):
        return self.title
