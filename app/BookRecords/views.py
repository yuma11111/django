from django.shortcuts import render
from django.http import HttpResponse

from .models import BookRecord, series

# Create your views here.
def index(request):
    BookList = BookRecord.objects.order_by("-id")
    context = {"BookList": BookList}
    return render(request, "BookRecords/index.html", context)