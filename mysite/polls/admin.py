from django.contrib import admin
from .models import Choice, Question

# Register your models here.

#
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


#モデルから取得した値のオプション（表示順など）を指定
class QuestionAdmin(admin.ModelAdmin):
    #fields = ["pub_date", "question_text"]
    fieldsets = [
        ("質問1", {"fields": ["question_text"]}), 
        ("登録日", {"fields": ["pub_date"], "classes": ["collapse"]}), 
    ]

    #一覧に表示するカラムの指定
    list_display = ["question_text", "pub_date", "was_published_recently"]

    #フィルタの追加
    list_filter = ["pub_date"]

    #検索欄の追加
    search_fields = ["question_text"]

    #
    inlines = [ChoiceInline]

#呼び出す際に第二引数で渡す
admin.site.register(Question, QuestionAdmin)
#質問とは別で選択肢の登録機能を追加
#admin.site.register(Choice)