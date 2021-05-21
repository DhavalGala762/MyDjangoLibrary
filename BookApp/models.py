from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class Book(models.Model):
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=False)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=25)
    ebook = models.FileField(upload_to='media')
    issued_date = models.DateField()

    def __str__(self):
        return self.title
    
    def clean(self):
        if self.title == "":
            raise ValidationError('Empty error message')