"""norsin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from home.views import index, search, about, contact
from blogs.views import blogs, post, post_create, post_update, post_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('', index, name='index'),
    path('search/', search, name='search'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('blogs/', blogs, name='blogs'),
    path('add/', post_create, name='post_create'),
    path('post/<slug>/', post, name='post_detial'),
    path('post/<slug>/update/', post_update, name='post_update'),
    path('post/<slug>/delete/', post_delete, name='post_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
