from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<book_id>\d+)/comment/$', views.comment, name='comment'),
    url(r'^about/$', views.about, name='home'),
    url(r'^25/$', views.top25, name='top25'),
    url(r'^book_detail/(?P<book_id>\d+)/$', views.detail, name='detail'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/success/$', views.register_success, name='register_success'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^account/success/$', views.set_account_success, name='set_account_success'),
    url(r'^account/(?P<username_slug>[\w\@\.\+\-\_]+)/$', views.set_account, name='set_account'),
    url(r'^book/search/$', views.search_book),
    url(r'^laber_detail/(?P<laber_title>.*)/$', views.laber_detail, name='laber'),
    url(r'^book/note/(?P<note_book_id>\d+)/$', views.notes, name='note_book'),
    url(r'^book/note_detail/(?P<note_book_id>\d+)/$', views.note_detail, name='note_detail'),
]