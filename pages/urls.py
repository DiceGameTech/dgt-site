from django.conf.urls import include, url
from . import views

app_name = 'pages'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
