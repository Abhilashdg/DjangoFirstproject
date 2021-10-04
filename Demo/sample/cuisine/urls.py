from django.conf.urls import url
from . import views
from django.urls import path
app_name = 'cuisine'
urlpatterns = [
     # Cuisine_list view as a function
     url(r'^$', views.CuisineListView.as_view(), name='cuisine_list_cls'),
     
     #url(r'^$',
     #views.Cuisine_list,
     #name='Cuisine_list'
     #),
     # Cuisine_detail view as a function
     url(r'^(?P<cuisine>[-\w]+)/$',
     views.Cuisine_detail,
     name='Cuisine_detail'
     ),
     url(r'^(?P<cuisine_id>\d+)/share/$',
         views.ShareCuisineViaEmail,
         name='cuisine_share'),
    ]
