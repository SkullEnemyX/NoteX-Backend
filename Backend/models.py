import datetime
from djongo import models

class Authentication(models.Model):
    username = models.CharField(max_length = 100)
    objects = models.Manager()
    password = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100,default = "user")
    email = models.EmailField(null = True)

    def __str__(self):
        return self.username
    
class Notes(models.Model):
    notesTitle = models.CharField(max_length = 100,default = " ")
    notesDesc = models.TextField(default = " ")
    class Meta:
        abstract = True

# class NoteForm(forms.ModelForm):
#     class Meta:
#         model = Notes
#         fields = ['notesTitle','notesDesc']

class NoteApp(models.Model):
    username =  models.CharField(max_length=100,primary_key=True)
    notesApp = models.ArrayModelField(
        model_container= Notes,
        default = []
    )
    objects = models.DjongoManager()

    def __str__(self):
        return self.username