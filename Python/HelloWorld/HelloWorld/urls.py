from django.conf.urls import url
 
from . import view
 
urlpatterns = [
    url(r'^123$', view.hello),
]