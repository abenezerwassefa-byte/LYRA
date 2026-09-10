from django.db import models


class Recording(models.Model):
    audio = models.FileField(upload_to="recordings")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="pending")
# Create your models here.
