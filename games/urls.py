from django.conf.urls import url,include
from . import views

app_name = 'games'
urlpatterns = [

    url(r'^$', views.IndexView.as_view(),name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view() ,name='detail'),

    #add
    url(r'paczka/add/$',views.PaczkaCreate.as_view(),name='paczka-add'),
    #update
    url(r'paczka/(?P<pk>[0-9]+)/$',views.PaczkaUpdate.as_view(),name='paczka-update'),
    #delete
    url(r'paczka/(?P<pk>[0-9]+)/delete/$',views.PaczkaDelete.as_view(),name='paczka-delete'),

     url(r'^login/$',views.login,name='login'),
    # url(r'^$',views.auth,name='auth_view'),
    url(r'^$',views.logout,name='logout'),
    url(r'^$',views.loggedin,name='loggedin'),
    url(r'^$',views.invalid_login,name='invalid_login'),




]
