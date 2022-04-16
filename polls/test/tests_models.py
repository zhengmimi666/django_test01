from django.test import TestCase

# Create your tests here.
#用来编写测试用例

from django.test import TestCase
from django.utils import timezone
from polls.models import Question,Choice
from django.test import Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class QuestionTestCase(TestCase):
    def setUp(self):
        Question.objects.create(id=1,question_text="go where?", pub_date=timezone.now())

    def test_question_query(self):
        """Animals that can speak are correctly identified"""
        #django在运行测试的时候不会使用数据库里的数据，所有测试数据都需要自己构造
        #缺点：数据要自己构造
        #优点：数据独立，不会干扰
        question = Question.objects.get(id=1)
        self.assertEqual(question.question_text, 'go where?')

    def test_question_create(self):
        """Animals that can speak are correctly identified"""
        Question.objects.create(id=2,question_text="when?", pub_date=timezone.now())
        question = Question.objects.get(id=2)
        self.assertEqual(question.question_text, 'when?')

    def test_question_update(self):
        """Animals that can speak are correctly identified"""
        question = Question.objects.get(id=1)
        question.question_text = "加班？"
        question.save()
        question = Question.objects.get(id=1)
        self.assertEqual(question.question_text, '加班？')

    def test_question_delete(self):
        """Animals that can speak are correctly identified"""
        #django在运行测试的时候不会使用数据库里的数据，所有测试数据都需要自己构造
        #缺点：数据要自己构造
        #优点：数据独立，不会干扰
        question = Question.objects.get(id=1)
        question.delete()
        question = Question.objects.all()
        self.assertEqual(len(question), 0)

class ChoiceTestCase(TestCase):
    def setUp(self):
        Question.objects.create(id=1,question_text="go where?", pub_date=timezone.now())
        Choice.objects.create(id=1,question_id=1,choice_text="hangzhou", votes=0)
        Choice.objects.create(id=2,question_id=1,choice_text="shanghai", votes=0)

    def test_choice_query(self):
        """Animals that can speak are correctly identified"""
        #django在运行测试的时候不会使用数据库里的数据，所有测试数据都需要自己构造
        #缺点：数据要自己构造
        #优点：数据独立，不会干扰
        question = Question.objects.get(id=1)
        choice = question.choice_set.get(id=1) #通过问题定位到选项
        # choice = Choice.objects.get(id=1)   #通过选项id定位到选项
        self.assertEqual(choice.choice_text, 'hangzhou')


    def test_choice_create(self):
        """Animals that can speak are correctly identified"""
        Choice.objects.create(id=3,question_id=1,choice_text="beijing", votes=0)
        choice = Choice.objects.get(id=3)
        self.assertEqual(choice.choice_text, 'beijing')

    def test_choice_update(self):
        """Animals that can speak are correctly identified"""
        choice = Choice.objects.get(id=1)
        choice.choice_text = "najing"
        choice.save()
        choice = Choice.objects.get(id=1)
        self.assertEqual(choice.choice_text, 'najing')

    def test_choice_delete(self):
        """Animals that can speak are correctly identified"""
        #django在运行测试的时候不会使用数据库里的数据，所有测试数据都需要自己构造
        #缺点：数据要自己构造
        #优点：数据独立，不会干扰
        choice1 = Choice.objects.get(id=1)
        choice2 = Choice.objects.get(id=2)
        choice1.delete()
        choice2.delete()
        choice = Choice.objects.all()
        self.assertEqual(len(choice), 0)






