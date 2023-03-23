#from django.urls import path
from . import views
from django.urls import include, re_path
#django.conf.urls.url() was deprecated in Django 3.0, and is removed in Django 4.0+.
#The easiest fix is to replace url() with re_path(). re_path uses regexes like url, so you only have to update the import and replace url with re_path.

urlpatterns = [
    #path('', views.index, name='index'),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    
]
