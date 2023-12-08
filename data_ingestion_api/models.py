from django.db import models

# Create your models here.

class Document(models.Model):
    name = models.CharField(max_length=255)
    document_type = models.CharField(max_length=100)
    file = models.FileField(upload_to='Users/jaideepreddyaluru/Documents/dest/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
