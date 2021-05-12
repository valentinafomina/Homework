from django.urls import path, include
from ..authapp import views as authapp

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('profile/', authapp.edit, name='edit'),
    path('register/', authapp.register, name='register')
]

app_name = "authapp"

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)