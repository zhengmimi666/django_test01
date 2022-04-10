# coding=utf-8
import unittest
# from test_sample import MyTest
# from test_sample2 import MyTest2
#
# #测试套件
# suit = unittest.TestSuite()
# suit.addTest(MyTest("test_add_1"))
# suit.addTest(MyTest("test_add_2"))
# suit.addTest(MyTest("test_add_3"))
# suit.addTest(MyTest2("test_add_1"))
# suit.addTest(MyTest2("test_add_2"))
# suit.addTest(MyTest2("test_add_3"))

suit = unittest.defaultTestLoader.discover("./test_dir","test_*.py")

#测试运行器
runner = unittest.TextTestRunner()
runner.run(suit)

