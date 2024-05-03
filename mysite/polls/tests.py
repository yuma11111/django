from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse

from .models import Question

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


#「QuestionModelTests(TestCase)」の書き方で「TestCase」を継承している。
#＝サブクラスになった という言い方をするらしい。
#モデル名＋Testsみたいな感じで命名すれば良さそう。
#python3 manage.py test pollsのコマンドを実行すると
#自動的に当該ファイルを見つけ出しクラス内に定義されているテストを実行してくれる
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "pollsは利用できません。")
        self.assetQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        question = create_question(question_text="過去の質問", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"], 
            [question], 
        )
    
    def test_future_question(self):
        create_question(question_text="未来の質問", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "pollsは利用できません。")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        question = create_question(question_text="過去の質問", days=-30)
        create_question(question_text="未来の質問", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"], 
            [question], 
        )
    
    def test_two_past_question(self):
        question1 = create_question(question_text="過去の質問1", days=-30)
        question2 = create_question(question_text="過去の質問2", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"], 
            [question1, question2], 
        )
    
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text="未来の質問", days=5)
        url = reverse("polls:detail", args=(future_question.id, ))
        response = self.client.get(url)
        self.asserEqual(response.status_code, 404)
    
    def test_past_question(self):
        past_question = create_question(question_text="過去の質問", days=-5)
        url = reverse("polls:detail", args=(past_question.id))
        response = self.client.get(uel)
        self.assertContains(response, past_question.question_text)
    
    



# Create your tests here.
