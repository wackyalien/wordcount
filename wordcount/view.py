from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
	return render(request,'home.html')
def about(request):
	return render(request,'about.html')
def count(request):
	fulltext = request.GET['fulltext']
	word = fulltext.split()
	return render(request,'count.html',{'fulltext':fulltext,'count':len(word)})

