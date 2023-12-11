from django.db import models

# Create your models here.
def upload_to(instance, filename):
    return f'Users/jaideepreddyaluru/Documents/dest/{filename}'

class Document(models.Model):
    name = models.CharField(max_length=255)
    document_type = models.CharField(max_length=100)
    file = models.FileField(upload_to='Users/jaideepreddyaluru/Documents/dest/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_file_url(self):
        return self.file.url
