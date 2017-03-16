from django.conf.urls import url
#from django.contrib import admin

from. import views as post_views

urlpatterns = [url(r'^$',post_views.posts_list),
    url(r'^create/$',post_views.posts_create),
    url(r'^detail/(?P<id>\d+)/$',post_views.posts_detail,name='detail'),
    #url(r'^list/$',post_views.posts_list),
    url(r'^update/$',post_views.posts_update),
    url(r'^delete/$',post_views.posts_delete),

    
]