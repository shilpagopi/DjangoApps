from django.urls import path

from .views import home_page_view,inline_html,pass_default_values_to_html,pass_values_from_url_to_html,execute_java,hello_world_view
from .form import input

urlpatterns = [
    path('', home_page_view, name='home_page_view'),
	path('helloworld/', hello_world_view, name='hello_world_view'),		
	path('inline_html/', inline_html, name='inline_html'),
	path('form/', input, name='form'),
	path('pass_default_values_to_html/', pass_default_values_to_html, name='pass_default_values_to_html'),
	path('pass_values_from_url_to_html/<int:num>/', pass_values_from_url_to_html, name='square html'),	
	path('java/', execute_java, name='execute_java')	
]
