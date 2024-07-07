from django.db.models import F
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse
from django.views import View

from .forms import regesterBookForm, updateBookForm
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
        
        aHave = {0:'持っていない',1:'買う予定',2:'持っている'}
        
        return render(request, 'BookRecords/confirm.html', {'form':form, 'aHave':aHave})

class BookUpdateView(generic.UpdateView):
    model = BookRecord      
    template_name = 'BookRecords/edit.html'
    form_class = updateBookForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse("BookRecords:update", kwargs={"pk":self.object.pk})

    def get(self, request, books_id):
        form = self.form_class
        #return render(request, 'BookRecords/edit.html', {'form':form, 'Books':Books})
        return render(request, 'BookRecords/edit.html', {'form':form})

    def post(self, request):
        if "list" in request.POST:
            #Books = get_object_or_404(BookRecord, pk=id)
            form = editBookForm()
            
        elif "edit" in request.POST:
            form = editBookForm(request.POST)
            #入力チェックに問題がない場合
            if form.is_valid():
                #確認画面へ遷移
                return render(request, 'BookRecords/edit_confirm.html', {'form':form})
        
        return render(request, 'BookRecords/edit.html', {'form':form, 'Books':Books})