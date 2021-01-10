import unittest
from login import get_pw,get_um

version=2.0
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('类执行前执行此命令')
    @classmethod
    def tearDownClass(cls) -> None:
        print('类执行后执行此命令')
    def setUp(self) -> None:
        print('用例执行前执行此命令')
    def tearDown(self) -> None:
        print('用例执行后执行此命令')
    @unittest.skipIf(version>1.0,'跳过此条用例')
    def u_name(self):
        except_name='zhh'
        result_name=get_um()
        self.assertEqual(except_name,result_name)
    def pa_word(self):
        except_name = '123456'
        result_name = get_pw()
        self.assertEqual(except_name,result_name)

# unittest.main()


#1、添加需要执行的测试用例的两个方法
#（1）使用TestSuite下的addTest或addTest方法添加要执行的测试用例
# 创建套件对象
# suite=unittest.TestSuite()
##添加单一用例
# suite.addTest(Login('u_name'))
# suite.addTest(Login('pa_word'))
#添加多个用例
# lst=[Login('u_name'),Login('pa_word')]
# suite.addTests(lst)
#（2）使用TestLoader下的discover方法添加要执行的测试用例
suite=unittest.TestLoader().discover('.',pattern='test*.py')

#2、通过TextTestRunner下的run方法去执行测试用例
runner=unittest.TextTestRunner()
runner.run(suite)