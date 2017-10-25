from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.splash, name='splash'),
    url(r'home', views.home, name='home'),
    url(r'about', views.about, name='about'),
    url(r'team', views.team, name='team'),
    url(r'katie', views.katie, name='katie'),
    url(r'leslie', views.leslie, name='leslie'),
    url(r'business', views.business, name='business'),
    url(r'contact', views.contact, name='contact'),
    url(r'winery', views.winery, name='winery'),
    url(r'ice_house', views.ice_house, name='ice_house'),
    url(r'contact', views.contact, name='contact'),
    url(r'purchase', views.purchase, name='purchase'),
    url(r'sparkling', views.sparkling, name='sparkling'),
    url(r'serendipity', views.serendipity, name='serendipity'),
    url(r'champenoise', views.champenoise, name='champenoise'),
    url(r'news', views.news, name='news'),
    url(r'event', views.event, name='event'),
    url(r'still_wine', views.still_wine, name='still_wine'),
]


