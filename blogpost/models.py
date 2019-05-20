from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class post(models.Model):
    heading = models.CharField(max_length = 200)
    upload_date = models.DateTimeField('Date of upload', default = timezone.now())
    content = models.TextField()

    def preview(self):
        return self.content[:250]

    def content_length(self):
        return len(self.content)
        
    def get_absolute_url(self):
        return reverse('Index')