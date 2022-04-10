# coding=utf-8
import unittest

#1.测试类必须继承unittest.TestCase
def add(a,b):
    return a+b

def setUpModule():
    print('== 模块开始')

def tearDownModule():
    print('== 模块开始')

class MyTest2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('所有用例执行之前执行')

    @classmethod
    def tearDownClass(cls):
        print('所有用例执行结束执行')

    def setUp(self):
        print('用例执行之前执行')

    def tearDown(self):
        print('用例执行结束执行')

    # 2.测试用例必须以"test"开头
    def test_add_1(self):
        # print('this is a case1')
        result = add(1,2)
        self.assertEqual(result,3)

    def test_add_2(self):
        # print('this is a case2')
        result = add(1.1,2.2)
        self.assertNotEqual(result,3.3)

    def test_add_3(self):
        # print('this is a case2')
        result = add(3,-1)
        self.assertEqual(result,2)

    def test_in_1(self):
        # print('this is a case2')
        self.assertIn('h','hello')



if __name__ == "__main__":
    # unittest.TestLoader().testMethodPrefix = "abc"  测试用例必须以"abc"开头,一般不建议更改
    unittest.main()
    #测试套件
    # suit = unittest.TestSuite()
    # suit.addTest(MyTest("test_add_1"))
    #测试运行器
    #测试运行器
    # runner = unittest.TextTestRunner()
    # runner.run(suit)

