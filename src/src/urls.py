from django.conf.urls import url
from django.contrib import admin
from apps.semestral.views import (LoginView, AsignaturaView, AsignaturaCrear)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', LoginView.as_view()),
    url(r'^asignaturas/', AsignaturaView.as_view()),
    url(r'^asignaturas/crear', AsignaturaCrear.as_view()),

]
