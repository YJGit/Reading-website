from django.shortcuts import render
from books.models import book

# Create your views here.
def home(request):
    book_list = []
    for id in range(1, 10):
        book_list.append(book.objects.get(book_id = id))
    return render(request,  'home.html', {'book_list': book_list, 'title': 'book_website',})