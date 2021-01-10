# 数据参数化
from parameterized import parameterized
import unittest
def add(x,y):
    return x+y

class Testadd(unittest.TestCase):
    @parameterized.expand([(1,2,3),(2,2,3),(1,3,4),(4,5,6)])
    def testadd(self,x,y,except_result):
        real_result=add(x,y)
        self.assertEqual(real_result,except_result)

if __name__ == '__main__':
    unittest.main()

