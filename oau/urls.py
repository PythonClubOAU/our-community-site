from django.conf.urls import url, include
from django.contrib import admin
from blog import views as blogview
from oau import views

urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^$', views.index, name="index"),
    url(r'^oau/$', views.index, name="index"),
    url(r'^blog/$', blogview.index, name='blog'),
]