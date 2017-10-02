# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .forms import TweetForm
from .passwordvalidator import PasswordStrengthEvaluator

def home(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = TweetForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			tweet = form.cleaned_data['tweet']
			password = PasswordStrengthEvaluator(tweet)
			result = password.evaluator()
			
			dict1={'result':result}        
			return render(request,"result.html",dict1)

	# if a GET (or any other method) we'll create a blank form
	else:
		form = TweetForm()

	return render(request, 'index.html', {'form': form})


def result(request,result):
    return render(request,'result.html')



