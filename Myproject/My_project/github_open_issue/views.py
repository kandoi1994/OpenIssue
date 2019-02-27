from django.shortcuts import render
from django.http import HttpResponse
from github_open_issue.test12 import *
# Create your views here.
def index(request):
	return render(request, 'github_open_issue/test.html')
	#return HttpResponse("<h1> This is 1vst app ")


def showResult(request,url):
	# import os
	# print(os.getcwd())
	date_test = test12()
	#date_test.fun1()
	#import pdb
	#pdb.set_treace()
	senttable = date_test.fun1(url)
	#print(senttable)
	return render(request, 'github_open_issue/test.html', {'senttable': senttable})

