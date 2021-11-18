from testCase import qqEmail_one;
import HTMLTestRunnerCN;
import unittest;
excase=unittest.defaultTestLoader.discover("../testCase","qqEmail_one.py");
report=open("../testReport/qqemailResult.html","wb");
runner=HTMLTestRunnerCN.HTMLTestRunner(stream=report,title="测试",description="描述");
runner.run(excase);