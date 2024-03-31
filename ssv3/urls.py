from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ssv3app.urls')),
    # Include your app's urls
    # path('', include('ssv3app.urls')),
    # ... any other URL configs
]
