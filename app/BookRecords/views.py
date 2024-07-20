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

    def post(self, request):
        return self.get(request)

class BooksDetailView(generic.DetailView):
    
    template_name = 'BookRecords/detail.html'
    model = BookRecord

    def get(self, request, books_id):
        book = get_object_or_404(BookRecord,pk=books_id)
        return render(request, 'BookRecords/detail.html', {'book':book, 'books_id':books_id})


class BooksRegesterView(View):        
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

class BooksUpdateView(generic.UpdateView):
    model = BookRecord      
    template_name = 'BookRecords/edit.html'
    form_class = updateBookForm

    def get(self, request, books_id):

        #DBから値を取得する
        #pkがWHERE句で指定するID
        book = get_object_or_404(BookRecord,pk=books_id)

        #formを設定。初期値として復元したい値を表示
        form = self.form_class(initial={'name': book.name, 'detail': book.detail, 'have': book.have, 'release_date': book.release_date})
        return render(request, 'BookRecords/edit.html', {'form':form,'book':book,'books_id':books_id})

    def post(self, request):
        if "edit" in request.POST:
            form = editBookForm(request.POST)
            #入力チェックに問題がない場合
            if form.is_valid():
                #確認画面へ遷移
                return render(request, 'BookRecords/edit_confirm.html', {'form':form})
        
        return render(request, 'BookRecords/edit.html', {'form':form, 'Books':Books})

class ConfirmView(View):
    template_name = 'BookRecords/confirm.html'
    model = BookRecord
    form_class = updateBookForm

    def post(self, request):
        # 新規登録 入力画面
        if "command" in request.POST:
            input_command = request.POST.get('command', None)

            #新規登録
            if input_command == '1':
                command = 'reg'
                books_id = ''
            #修正
            elif input_command == '2':
                command = 'edit'
                if 'books_id' in request.POST:
                    books_id = request.POST.get('books_id', None)
            
            form = regesterBookForm(request.POST)
            return render(request, 'BookRecords/confirm.html', {'form':form, 'command':command, 'books_id':books_id})

        else:
            #新規登録
            if "reg" in request.POST:
                form = regesterBookForm(request.POST)
                if "name" in request.POST:
                    #入力チェックに問題がない場合
                    if form.is_valid():
                        form.save(commit=True)
                        #一覧画面へ遷移
                        return redirect('/BookRecords/')
            #修正
            elif "edit" in request.POST:
                books_id = request.POST.get('books_id', None)
                book = get_object_or_404(BookRecord,pk=books_id)
                form = updateBookForm(request.POST, instance=book)
                #入力チェックに問題がない場合
                if form.is_valid():
                    form.save(commit=True)
                    #修正対象の詳細画面に遷移
                    return redirect('/BookRecords/detail/'+books_id)
            
            #削除
            elif "delete" in request.POST:
                books_id = request.POST.get('books_id', None)
                book = get_object_or_404(BookRecord, pk=books_id)
                book.delete()
                return redirect('/BookRecords/')
    
    #削除
    def get(self, request, books_id):
        book = get_object_or_404(BookRecord,pk=books_id)
        form = self.form_class(initial={'name': book.name, 'detail': book.detail, 'have': book.have, 'release_date': book.release_date})
        return render(request, 'BookRecords/confirm.html', {'form':form, 'books_id':books_id, 'command':'delete'})
