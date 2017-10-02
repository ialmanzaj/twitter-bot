from django.conf.urls import url, include
from django.contrib import admin

from tweets.views import home, result

app_name = 'twitter-bot'


urlpatterns = [
	url(r'^$', home, name='index'),
	url(r'^result/$', result, name='result'),
	
    url(r'^admin/', admin.site.urls),
]
