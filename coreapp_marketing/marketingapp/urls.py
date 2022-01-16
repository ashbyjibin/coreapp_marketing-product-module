from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^TL_dash/$', views.TL_dash, name="TL_dash"),
    re_path(r'^TL_mytasks/$', views.TL_mytasks, name="TL_mytasks"),
    re_path(r'^TL_cardslist/$', views.TL_cardslist, name="TL_cardslist"),
    re_path(r'^TL_messagecards/$', views.TL_messagecards, name="TL_messagecards"),
    re_path(r'^TL_table/$', views.TL_table, name="TL_table"),
  

    # Marketing Executive
 
    re_path(r'^$', views.exec_mytasks, name="exec_mytasks"),
    re_path(r'^exec_products/$', views.exec_products, name="exec_products"),
    re_path(r'^exec_productdetails/(?P<id>\d+)$', views.exec_productdetails, name="exec_productdetails"),
    re_path(r'^exec_productdata/(?P<id>\d+)$', views.exec_productdata, name="exec_productdata"),
    re_path(r'^exec_savedc/(?P<id>\d+)$', views.exec_savedc, name="exec_savedc"),
    re_path(r'^exec_savedc1/(?P<st>\d+)$', views.exec_savedc1, name="exec_savedc1")
    


]