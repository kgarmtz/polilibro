"""Book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin, sitemaps
from django.conf.urls.static import static
from django.urls import path, include, re_path
# SEO stuff
from django.contrib.sitemaps.views import sitemap
from applications.home.sitemap import (
    SectionSitemap,
    Sitemap
)

# Our main urls
urlpatterns_main = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('polilibroescom/', admin.site.urls),
    path('recurso-digital/', include('applications.book.urls')),
    path('', include('applications.home.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns_main += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Create the Sitemap object that generates the XML file
sitemaps = {
    # The url structure is based on the main page of the site 'main.html' -- main url
    'site': Sitemap(
        [
            'home_app:index'
        ]
    ),

    # Subsequents url
    'secciones': SectionSitemap
}

urlpatterns_sitemap = [
    path(
        'sitemap.xml', 
        sitemap, 
        {'sitemaps': sitemaps},
        name = 'django.contrib.sitemaps.views.sitemap'
    ),
]


urlpatterns = urlpatterns_main + urlpatterns_sitemap