from django.db import models

# Create your models here.

# models 对应数据库 ORM
# python--->   ORM  ---->  数据库驱动  ---> SQLite
#ORM 无需写sql语句，可以像操作类方法一样操作数据库。
# 首先按照ORM方法定义表

'''
CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);'''



from django.db import models

import datetime
from django.utils import timezone

# class COMPANY(models.Model):
#     id = models.IntegerField()  #id不需要定义，自动加上
#     NAME = models.CharField(max_length=255)
#     AGE = models.IntegerField()
#     ADDRESS = models.CharField(max_length=50)



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_dete >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text