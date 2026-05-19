from django.shortcuts import render, redirect
from .models import Note

def notes_home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Note.objects.create(title=title, content=content)
        return redirect('notes_home')
        
    all_notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/index.html', {'notes': all_notes})

def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect('/')