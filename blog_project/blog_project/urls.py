#Project Level URL redirects

# blog_project/urls.py
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog_app.urls')),
    url(r'', include('blog_app.urls')),
    url(r'^signup', include('register_app.urls')),
]
