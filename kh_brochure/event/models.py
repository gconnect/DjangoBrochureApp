from django.db import models
from django.db import  models
# Register your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    event_image = models.FileField(upload_to='uploads')
    event_date = models.DateTimeField('Event Date')
    created_at = models.DateTimeField('published date')