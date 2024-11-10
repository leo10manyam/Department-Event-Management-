
# Create your models here.
from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event_type = models.CharField(max_length=50)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.event_type}'
