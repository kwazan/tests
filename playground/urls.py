from django.urls import path
from playground import views

#URLConf
urlpatterns = [
path('hello/', views.do_smtg),
path('hello/hello2/', views.do_smtg2, name="do_smtg2" ),
path('hello/hello3/', views.do_smtg3, name="do_smtg3"),
path('hello/success', views.success, name='success'),
path('blocked/', views.blocked, name="blocked")

]
