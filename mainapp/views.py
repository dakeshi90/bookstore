from django.shortcuts import render_to_response
from mainapp.models import Book

# Create your views here.
def latest_books(request):
    book_list = Book.objects.order_by('-pub_date')[:10]
    return render_to_response('latest_book.html', {'book_list' : book_list})