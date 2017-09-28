from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/orig') # original image
    filtered_image = models.ImageField(upload_to='uploads/%Y/%m/%d/filtered') # modified image
    content = models.TextField(max_length=500, null=True, blank=True) # text
    created_at = models.DateTimeField(auto_now_add=True) # created datetime
