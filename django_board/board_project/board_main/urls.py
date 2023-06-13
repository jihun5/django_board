from django.urls import path
from . import views_test

urlpatterns = [   
   path('', views_test.test_html_multi_data),
   path('test_json', views_test.test_json_data),
   path('parameter_data', views_test.test_html_parameter_data),


]
