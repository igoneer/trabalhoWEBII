from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^menu/$', views.MenuView.as_view(), name='menu'),
    url(r'^blog/$', views.BlogView.as_view(), name='blog'),
    url(r'^events/$', views.EventsView.as_view(), name='events'),
    url(r'^single/$', views.SingleView.as_view(), name='single'),
    url(r'^typo/$', views.TypoView.as_view(), name='typo'),
]

