from django.conf.urls import url
from django.contrib import admin
from semestral.views import (HomeView, ContactsView)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', HomeView.as_view()),
    url(r'^index/contacts/$', ContactsView.as_view()),

]
