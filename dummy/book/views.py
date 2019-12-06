from django.shortcuts import render

from django.http import HttpResponse


def about_book(request):
    return render(request,'book/book.html')

def books(request):
	context={
		'books':books
	}
	return render(request,'user/home.html',context)


