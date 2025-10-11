from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    """Форма для создания и обновления заметок."""

    class Meta:
        model = Note
        fields = ('title', 'description')
