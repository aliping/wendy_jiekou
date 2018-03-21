# coding:utf-8
from common import HTMLTestRunner
import unittest
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 获取用例所在的文件路径
casePath = os.path.join(os.getcwd(),"case")
print(casePath)

# discover加载所在路径下的所有用例
discover = unittest.defaultTestLoader.discover(casePath,
                                        pattern="test*.py",
                                        )


if __name__ == "__main__":
    # 获取报告的生成路径和名称
    reportPath=os.path.join(os.getcwd(),"report\\result.html")
    # 以二进制的方式写入并打开报告
    fp=open(reportPath,"wb")
    # HTMLTestRunner.HTMLTestRunner()表示HTMLTestRunner模块中的HTMLTestRunner类
    # verbosity=2表示显示用例描述的详细程度
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                         verbosity=2,
                                         title=u"禅道登录测试用例",
                                         description=u"禅道登录用例执行情况："
                                         )
    runner.run(discover)