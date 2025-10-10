from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    """Форма для создания и обновления заметок."""

    model = Note
    fields = ('title', 'description')
