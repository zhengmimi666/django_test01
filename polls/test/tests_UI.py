from django.test import TestCase

# Create your tests here.
#用来编写测试用例

from django.test import TestCase
from django.utils import timezone
from polls.models import Question,Choice
from django.test import Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By



class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.self.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        Question.objects.create(id=1,question_text="go where?", pub_date=timezone.now())
        Choice.objects.create(id=1,question_id=1,choice_text="hangzhou", votes=0)
        Choice.objects.create(id=2,question_id=1,choice_text="shanghai", votes=0)

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/polls/'))
        front_vote_number = self.selenium.find_elements(By.XPATH,"//div[@class='progress']/p")[0].text 
        self.selenium.find_element(By.ID,"1").click()
        self.selenium.find_element(By.XPATH,"//input[@type='radio' and @value='1']").click() #not much
        self.selenium.find_element(By.ID,"voteButton").click()  #boteButton
        after_vote_number = self.selenium.find_elements(By.XPATH,"//div[@class='progress']/p")[0].text  #boteButton
        print(after_vote_number)
        self.assertEqual(front_vote_number,after_vote_number)




