# Create your views here.
from django.shortcuts import render
from books.models import Book
from django.http import HttpResponse

def search(request):
	errors = [] 
	if 'q' in request.GET: 
		q = request.GET['q']
		if not q: 
			errors.append('Enter a saerch term.') 
		elif len(q) > 20:
			errors.append('Please enter at most 20 characters.')
		else: 
			books = Book.objects.filter(title__icontains=q)
			return render(request, 'search_results.html', 
			{'books': books, 'query': q})
	
	# does not redirect you to new page -- error on top of search bar
	return render(request, 'search_form.html', {'errors': errors})
