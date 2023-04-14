from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Contact(models.Model):
    vorname = models.CharField(max_length=100)
    nachname = models.CharField(max_length=100)
    email = models.EmailField()
    unternehmen = models.CharField(max_length=100)
    # nachricht = models.CharField(widget=models.Textarea)
    nachricht = models.TextField()
    def __str__(self):
        return self.vorname + " " + self.nachname 