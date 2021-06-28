from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include

#SE AGREGAN LAS RUTAS DEL PROYECTO GENERAL (LLAMADO DOCKER)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('post.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('post.urls')),	
    path('oauth/', include('social_django.urls', namespace='social')),
    path('accounts/', include('allauth.urls')),
    url(
        r'^social/',
        include('social.apps.django_app.urls', namespace='social')
    ),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
]

#AGREGA LOS ARCHIVOS DE LA BASE DE DATOS 
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)