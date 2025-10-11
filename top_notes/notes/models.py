from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


User = get_user_model()


class Note(models.Model):
    """Модель заметки."""

    title = models.CharField(
        'Заголовок',
        max_length=100,
        help_text='Заголок заметки',
        null=True,
        blank=True,
        db_index=True,
    )
    description = models.TextField(
        'Текст заметки',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор заметки',
        related_name='notes',
    )

    class Meta:
        verbose_name = 'Заметки'
        verbose_name_plural = 'Заметки'
        ordering = ['-updated_at']

    def get_absolute_url(self):
        return reverse("notes:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
