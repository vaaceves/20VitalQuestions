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
from questions.views import logout, index_spa, index_eng, LoginUserViewSpa, LoginUserViewEng, topic_spa, topic_eng, contact_eng, contact_spa, about_eng, about_spa, question_eng, question_spa, all_videos_eng, all_videos_spa

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$',logout, name='logout'),
    # ENGLISH URLS
    url(r'^$', index_eng, name='index_eng'),
    url(r'^en/login/$', LoginUserViewEng.as_view(), name='login_eng'),
    url(r'^en/(?P<slug>[\w\-]+)/$', topic_eng, name='topic_eng'),
    url(r'^en/view/(?P<slug>[\w\-]+)/$', question_eng, name='question_eng'),
    url(r'^en/contact', contact_eng, name='contact_eng'),
    url(r'^en/about', about_eng, name='about_eng'),
    url(r'^en/videos', all_videos_eng, name='all_videos_eng'),
    # SPANISH URLS
    url(r'^es/$', index_spa, name='index_spa'),
    url(r'^es/login/$', LoginUserViewSpa.as_view(), name='login_spa'),
    url(r'^es/(?P<slug>[\w\-]+)/$', topic_spa, name='topic_spa'),
    url(r'^es/view/(?P<slug>[\w\-]+)/$', question_spa, name='question_spa'),
    url(r'^es/contact', contact_spa, name='contact_spa'),
    url(r'^es/about', about_spa, name='about_spa'),
    url(r'^es/videos', all_videos_spa, name='all_videos_spa'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = '20 Vital Questions'
