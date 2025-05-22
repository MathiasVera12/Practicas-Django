from django.db import models

# Create your models here.
class Note(models.Model):
    noteId = models.IntegerField(primary_key=True)
    noteDate = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=50)
    
    def __str__(self):
        return self.note
