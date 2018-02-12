from django.conf.urls import url
from adminLTE_template import views as adminlte_template_views

urlpatterns = [
    url(r'^admin/$', adminlte_template_views.home),
]