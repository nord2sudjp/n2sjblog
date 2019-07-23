from django.contrib import admin
from django.urls import path, include
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path(settings.HOME_URL, views.home, name='home'),
    path(settings.HOME_URL + 'blog/', include('blog.urls')),
    path(settings.HOME_URL + 'accounts/', include('accounts.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
      + static(settings.CSS_URL, document_root=settings.CSS_ROOT) \
      + static(settings.SCRIPT_URL, document_root=settings.SCRIPT_ROOT)
