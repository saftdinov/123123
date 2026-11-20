from django.views import generic
from django.shortcuts import render
from django.db.models import Q
from .models import Book, Author, BookInstance, Genre


def index(request):
    context = {
        "num_books": Book.objects.count(),
        "num_instances": BookInstance.objects.count(),
        "num_instances_available": BookInstance.objects.filter(status__exact="a").count(),
        "num_authors": Author.objects.count(),
        "num_genres": Genre.objects.count(),
    }
    return render(request, "catalog/index.html", context)


class BookListView(generic.ListView):
    model = Book
    template_name = "catalog/book_list.html"
    context_object_name = "book_list"
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "catalog/book_detail.html"


class AuthorListView(generic.ListView):
    model = Author
    template_name = "catalog/author_list.html"
    context_object_name = "author_list"
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = "catalog/author_detail.html"


def search(request):
    query = request.GET.get("q", "").strip()
    results = Book.objects.filter(
        Q(title__icontains=query) | Q(author__first_name__icontains=query) |
        Q(author__last_name__icontains=query)
    ) if query else Book.objects.none()
    return render(request, "catalog/search.html", {"query": query, "results": results})
