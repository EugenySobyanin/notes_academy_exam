from django.urls import path

from notes import views


app_name = 'notes'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('add/', views.NoteCreate.as_view(), name='add'),
    path('edit/<int:note_id>/', views.NoteUpdate.as_view(), name='edit'),
    path('note/<int:note_id>/', views.NoteDetail.as_view(), name='detail'),
    path('delete/<int:note_id>/', views.NoteDelete.as_view(), name='delete'),
    path('notes/', views.NotesList.as_view(), name='list'),
    path('done/', views.NoteSuccess.as_view(), name='success'),
]
