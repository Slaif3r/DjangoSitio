from django.conf.urls import url
from django.contrib import admin
from apps.semestral.views import (LoginView)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', LoginView.as_view()),
    #url(r'^index/contacts/$', ContactsView.as_view()),

]
