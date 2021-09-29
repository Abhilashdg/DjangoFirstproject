from django.conf.urls import url
from . import views
urlpatterns = [
     # Cuisine_list view as a function
     url(r'^$',
     views.Cuisine_list,
     name='Cuisine_list'
     ),
     # Cuisine_detail view as a function
     url(r'^(?P<cuisine>[-\w]+)/$',
     views.Cuisine_detail,
     name='Cuisine_detail'
     ),
    ]
