from django.conf.urls import url
from Complaintapp import views

app_name="Complaintapp"

urlpatterns=[
    url(r'^homepage/$',views.HomePage,name='homepage'),
    url(r'^about/$',views.About,name='about'),
    url(r'^info/$',views.Info,name='info'),
    url(r'^warden/$',views.Warden,name='warden'),
    url(r'^details/$',views.Details,name='details'),
]