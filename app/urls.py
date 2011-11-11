from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    (r'^$',index),
    (r'^department/(\w+)$',department),
)


