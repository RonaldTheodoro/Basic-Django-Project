from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),
    # Core app
    url(r'^', include('apps.core.urls', namespace='core')),
    # Accounts app
    url(r'^accounts/', include('apps.accounts.urls', namespace='accounts')),
]
