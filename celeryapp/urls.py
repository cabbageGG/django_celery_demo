from django.conf.urls import url
import views

urlpatterns = (
    url(r'^1/$', views.run_task),
)
