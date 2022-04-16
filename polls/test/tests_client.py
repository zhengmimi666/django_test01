from django.test import TestCase

# Create your tests here.
#用来编写测试用例

from django.test import TestCase
from django.utils import timezone
from polls.models import Question,Choice
from django.test import Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class IndexTestCase(TestCase):

    def setUp(self):
        Question.objects.create(id=1,question_text="go where?", pub_date=timezone.now())
        Choice.objects.create(id=1,question_id=1,choice_text="hangzhou", votes=0)
        Choice.objects.create(id=2,question_id=1,choice_text="shanghai", votes=7777)

    def test_index_page(self):
        #测试问题列表页
        response = self.client.get('/polls/')
        # print(response.content)
        self.assertEqual(response.status_code,200)
        self.assertIn(b"go where?",response.content)
        self.assertTemplateUsed(response,'polls/base_page.html')

    def test_detail_page(self):
        #测试问题详情页
        response = self.client.get('/polls/1/')
        # print(response.content)
        self.assertEqual(response.status_code,200)
        self.assertIn(b"hangzhou",response.content)
        self.assertIn(b"shanghai",response.content)
        self.assertTemplateUsed(response,'polls/detail.html')

    def test_result_page(self):
        #测试投票结果页
        response = self.client.get('/polls/1/results/')
        # print(response.content)
        self.assertEqual(response.status_code,200)
        self.assertIn(b"hangzhou",response.content)
        self.assertIn(b"shanghai",response.content)
        #验证投票数字
        self.assertIn(b"7",response.content)
        self.assertTemplateUsed(response,'polls/results.html')

    def test_vote_action(self):
        #测试投票动作页
        response = self.client.post('/polls/1/vote/',data={"choice":2})
        self.assertEqual(response.status_code,302)
        response = self.client.get('/polls/1/results/')
        self.assertIn(b"7778",response.content)



