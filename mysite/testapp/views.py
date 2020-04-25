from django.shortcuts import render
import textwrap
# Create your views here.

from django.http import HttpResponse
from subprocess import Popen, PIPE, STDOUT

def hello_world_view(request):
    return HttpResponse("Hello World!")
	
def home_page_view(request):
	return render(request, 'homepage.html')
	
def inline_html(request):
    response_text = textwrap.dedent('''\
            <html>
            <body>
                <p>Hi! This is an inline html rendering! </p>
            </body>
            </html>
        ''')
    return HttpResponse(response_text)

def pass_values_from_url_to_html(request,num):
	return render(request, 'result.html', {'num': num, 'val': num*num})

def pass_default_values_to_html(request,num=3):
	return HttpResponse("<p> %s </p>" %(str(num*num)))
	
def execute_java(request):	
	p = Popen(['java', '-jar', 'untitled.jar'], stdout=PIPE, stderr=STDOUT)
	#for line in p.stdout:
    #print line
	return HttpResponse(p.stdout)
	