from django.shortcuts import render, HttpResponse
from datetime import datetime
from BookApp.models import Book
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    return render(request, "index.html")

def View_Books(request):
    obj = Book.objects.all()
    
    return render(request, "View_Books.html", {'records':obj})

def Add_Books(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        ebook = request.FILES['ebook']
        book = Book(title = title, author = author, genre = genre, ebook =ebook, issued_date = datetime.today())
        book.full_clean()
        book.save()
        messages.success(request, 'Books details successfully Added.')
    return render(request, "Add_Books.html")



  
    