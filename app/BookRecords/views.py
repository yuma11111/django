from django.db.models import F
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse
from django.views import View

from .forms import regesterBookForm
from .models import BookRecord, series

# Create your views here.
class IndexView(generic.ListView):
    
    template_name = 'BookRecords/index.html'
    context_object_name = 'BookList'

    def get_queryset(self):
        return BookRecord.objects.order_by("-id")
        #context = {"BookList": BookList}
        #return render(request, "BookRecords/index.html", context_object_name)

    def post(self, request):
        return self.get(request)

class RegesterView(View):        
    template_name = 'BookRecords/reg.html'

    def post(self, request):
        if "list" in request.POST:
            form = regesterBookForm()
            
        elif "reg" in request.POST:
            form = regesterBookForm(request.POST)
            #入力チェックに問題がない場合
            if form.is_valid():
                #確認画面へ遷移
                return render(request, 'BookRecords/confirm.html', {'form':form})
        
        return render(request, 'BookRecords/reg.html', {'form':form})


class ConfirmView(View):
    template_name = 'BookRecords/confirm.html'

    def post(self, request):
        form = regesterBookForm(request.POST)
        if "confirm" in request.POST:
            if "name" in request.POST:
                #入力チェックに問題がない場合
                if form.is_valid():
                    form.save(commit=True)
                    #確認画面へ遷移
                
                return redirect('/BookRecords/')
        
        return render(request, 'BookRecords/confirm.html', {'form':form})
