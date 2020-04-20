import unittest
import requests
from requests import RequestException
from unittest import TestCase, main
from BeautifulReport import BeautifulReport

from test.test_data import NONE_DATA


def func(n):
    return n+1


# 在UnitTest中，都是通过方法名来识别是不是测试用例的。
#   所以测试用例的命名必须是由 "test" 开头。 例 def test_abc()
# 用例执行顺序：
    # 默认 按用例名字 “test” 后面字符顺序排列 0-9 a-z的顺序。
    # 自定义  使用 suite 设置，suite = unittest.TestSuite()

class myTest(unittest.TestCase):
    cookie = None
    headers = None
    # def __init__(self):
    #     self.cookie = None
    #     self.headers = None
    #     super(myTest, self).__init__()

    def set_cookie(self, response):
        if response.cookie is not None:
            self.cookie = response.cookie

    # 类的前置函数,整个类的所有实例执行前，先执行
    @classmethod
    def setUpClass(cls) -> None:
        print('sclass')

    # 类的后置函数，整个类的所有实例执行结束，再执行
    @classmethod
    def tearDownClass(cls) -> None:
        print('tclass')

    # 实例的初始化，就是前置中间件
    def setUp(self):
        print('setUp!!!')
        self.headers = {
            'cookie': self.cookie,
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.163 Safari/537.36',
            'content-type': 'application/json; charset=UTF-8'
        }

    # 实例的释放，后置中间件
    def tearDown(self):
        print("tearDown!!!")

    def test_nihao1(self):
        url = 'http://localhost:3278/root/index.json'
        for a in NONE_DATA:
            params = {
                'a': a,
                'b': a
            }
            try:
                req = requests.post(url=url, data=params, headers=self.headers)
                req_data = req.json()
                self.assertEqual(req_data.get('code'), 200, msg=req_data.get('msg'))
            except RequestException as e:
                self.assertFalse(True, msg=e.msg)
            except Exception as e:
                self.assertFalse(True, msg=e.msg)

    def test_nihao2(self):
        print(2)
        self.assertEqual(func(4), 7)

        self.assertEqual(1, 2, msg='msg')  # 断言两者是否相等,判断不成立时返回msg
        self.assertNotEqual(1, 2, msg='msg')  # 断言两者是否不相等,判断不成立时返回msg
        self.assertFalse(2, msg='msg')  # 判断参数是否为False,判断不成立时返回msg
        self.assertTrue(2, msg='msg')  # 判断参数是否为True,判断不成立时返回msg

    # 跳过执行当前测试用例，参数:提示msg
    @unittest.skip('msg,不想执行这条测试')
    # # 根据条件是否跳过，条件成立时跳过执行 参数：1、True 跳过，False 不跳过。2 跳过执行时，提示msg
    # @unittest.skipIf(1 > 2, reason='msg,条件不成立，所以不执行')
    # # 根据条件是否跳过，与skipIf相反，条件不成立时跳过，参数：1、True 不跳过，False 跳过。2 跳过执行时，提示msg
    # @unittest.skipUnless(1 > 2, reason='msg,条件不成立，所以不执行')
    def test_nihao3(self):
        print(3)
        self.assertEqual(func(4), 6)

    # @unittest.expectedFailure  # 测试用例执行报错时，不记录错误。预知报错。
    def test_nihao4(self):
        print(4)
        self.assertEqual(func(4), 5)


# if __name__ == "__main__":
#     # 调用unittest.main() 运行所有测试用例。
#     unittest.main()


# suite 运行测试用例
suite = unittest.TestSuite()

# 五种添加测试用例到suite中
# 一 、按顺序添加需要运行的测试用例
suite.addTest(myTest('test_nihao4'))
suite.addTest(myTest('test_nihao2'))
suite.addTest(myTest('test_nihao1'))

# # 二、批量添加test
# cases = [myTest('test_nihao4'), myTest('test_nihao2'), myTest('test_nihao1')]
# suite.addTests(cases)
#
# # 三、通过读取文件添加
# #   参数：start_dir 相对本项目的根路径
# #        pattern 文件名匹配
# suite = unittest.defaultTestLoader.discover(start_dir='../', pattern='test*.py')
#
# # 四、单独添加某个，文件或者类下的测试用例
# cases = unittest.TestLoader().loadTestsFromTestCase(myTest)  # 根据类名导入
# # cases = unittest.TestLoader().loadTestsFromName('test_unit')  # 根据文件名导入
# # cases = unittest.TestLoader().loadTestsFromNames('docker_web')  # 根据文件夹名导入
# suite.addTests(cases)
#
#
# # 初始化runner，main()其实也是run一个实例化的runner
# runnerm = unittest.TextTestRunner()
# # 使用runner.run运行suite
# runnerm.run(suite)  # == main()


# # 使用BeautifulReport 执行suite 来生成测试报告
# 报告存放地址
log_path = './report/'
# 测试报告名称
filename = '测试报告-百度'
# 用例描述
description = '百度登录'

result = BeautifulReport(suite)
result.report(filename=filename, description=description, log_path=log_path)


