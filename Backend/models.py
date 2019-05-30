import datetime
from djongo import models
from django import forms

class Authentication(models.Model):
    username = models.CharField(max_length = 100)
    objects = models.Manager()
    password = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100,null = True)
    email = models.EmailField(null = True)

    def __str__(self):
        return self.username
    
class Notes(models.Model):
    notesTitle = models.CharField(max_length = 100)
    notesDesc = models.TextField()
    objects = models.Manager()
    class Meta:
        abstract = True

class NoteApp(models.Model):

    objects = models.Manager()
    username =  models.CharField(max_length=100)
    notesApp = models.ArrayModelField(
        model_container= Notes,
        default = [],
        
    )

    def __str__(self):
        return self.username