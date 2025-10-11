from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import CreateView

from users.forms import CustomUserCreationForm


urlpatterns = [
    path('', include('notes.urls')),
    path('admin/', admin.site.urls),
]

auth_urls = ([
    path(
        'login/',
        auth_views.LoginView.as_view(),
        name='login',
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(
            template_name='registration/logout.html'
        ),
        name='logout',
    ),
    path(
        'signup/',
        CreateView.as_view(
            form_class=CustomUserCreationForm,
            success_url='/',
            template_name='registration/signup.html',
        ),
        name='signup'
    ),
], 'users')

urlpatterns += [path('auth/', include(auth_urls))]