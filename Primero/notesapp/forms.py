from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note']
        widgets = {
            'note': forms.TextInput(attrs={'class': 'form-control'}),
        }