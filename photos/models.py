from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import get_user_model
from django.conf import settings

class Photo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    image = models.ImageField(upload_to='%Y/%m/%d/orig') # original image
    filtered_image = models.ImageField(upload_to='%Y/%m/%d/filtered') # modified image
    content = models.TextField(max_length=500, null=True, blank=True) # text
    created_at = models.DateTimeField(auto_now_add=True) # created datetime

    class Meta:
        ordering = ('-created_at','-pk', )

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.filtered_image.delete()
        super(Photo, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        url = reverse_lazy('detail', kwargs={'pk': self.pk})
        return url
