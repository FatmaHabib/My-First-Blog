from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.chat_list, name='chat_list'),
]
