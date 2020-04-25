from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

FRUIT_CHOICES= [
    ('Oranges', 'Orange'),
    ('Cantaloupes', 'Cantaloupe'),
    ('Mangoes', 'Mango'),
    ('Honeydews', 'Honeydew'),
    ]
	
class InputForm(forms.Form):
	name = forms.CharField(max_length=100, label='Your Name')
	#email = forms.EmailField(required=False,label='Your e-mail address')
	message = forms.CharField(widget=forms.Textarea,required=False)
	fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=FRUIT_CHOICES))
	number = forms.IntegerField(label="Input number")

def input(request):
	submitted = False
	if request.method == 'POST':
		form = InputForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			# assert False
			# return HttpResponseRedirect("/square/%s/" % cd['message'])
			return render(request, 'form_result.html', {'num': cd['number'], 'val': cd['number']*cd['number'],'name':cd['name'],'fruit':cd['fruit']})
			#return HttpResponseRedirect('/thanks/')
	else:
		form = InputForm(initial={'name': 'Shilpa'})
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'form.html', {'form': form})