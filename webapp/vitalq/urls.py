"""vitalq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from questions.views import logout, index_spa, index_eng, LoginUserViewSpa, LoginUserViewEng

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$',logout, name='logout'),
    # ENGLISH URLS
    url(r'^$', index_eng, name='index_eng'),
    url(r'^en/login/$', LoginUserViewEng.as_view(), name='login_eng'),
    # SPANISH URLS
    url(r'^es/$', index_spa, name='index_spa'),
    url(r'^es/login/$', LoginUserViewSpa.as_view(), name='login_spa'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = '20 Vital Questions'
