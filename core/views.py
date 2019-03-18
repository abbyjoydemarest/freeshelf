from django.shortcuts import render, get_object_or_404
from core.models import Book, Author, Category, Favorite
from django.views import generic
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """View for the index(homepage) of the project. """
    #Count all of each model so we can use them moving forward
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_categories = Category.objects.all().count()
    category_list = Category.objects.all()
    favorite = Favorite.objects.all()
    #tell it how to provide in the information each section of the dictionary is used for a different reason.
    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_categories': num_categories,
        'category_list': category_list,
        'favorite': favorite,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate = 5

class BookDetailView(generic.DetailView):
    model = Book
    favorite = Favorite.objects.all() 

class CategoryListView(generic.ListView):
    model = Category
    category_list = Category.objects.all()

#set it up so that it is a POST method instead of a GET method
@require_http_methods(['POST'])
#require that the person be logged in to favorite a book
@login_required
#make this view a function because you need specify it as a POST
def book_favorite_view(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)

    next = request.POST.get('next', '/')

    #do this to get a boolean so we can see if this was the first time 
    #this person favorited the book or if they already favorited it 
    #then say it has been favorited
    favorite, created = request.user.favorite_set.get_or_create(book=book)

    if created:
        messages.success(request, f"You have favorited {book.title}.")
    else:
        messages.info(request, f"You have unfavorited {book.title}.")
        favorite.delete()
    #redirect it to the next page
    return HttpResponseRedirect(next)

def my_favorites_view(request):
    favorites = Favorite.objects.all()
    book_list = Book.objects.all()

    context = {
        'favorites': favorites,
        'book_list': book_list,
    }

    return render(request, 'core/book_favorite.html', context=context)
