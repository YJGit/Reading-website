from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<book_id>\d+)/$', views.detail, name='detail'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/success/$', views.register_success, name='register_success'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^account/success/$', views.set_account_success, name='set_account_success'),
    url(r'^account/(?P<username_slug>[\w\@\.\+\-\_]+)/$', views.set_account, name='set_account'),
    url(r'^(?P<laber_title>.*)/$', views.laber_detail, name='laber'),
]