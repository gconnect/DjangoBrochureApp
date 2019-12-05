from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    course_image = models.FileField(upload_to='uploads')
