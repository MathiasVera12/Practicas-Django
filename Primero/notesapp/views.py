from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm

# Create your views here.
def index(request):
    notes = Note.objects.all().order_by('-noteDate')
    return render(request, 'notesapp/list.html', {'notes': notes})

def new_note(request):
    if request.method == 'POST':
        formulario = NoteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('list')
    else:
        formulario = NoteForm()
    
    return render(request, 'notesapp/new_note.html', {'formulario': formulario})


