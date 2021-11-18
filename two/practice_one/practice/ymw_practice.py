import unittest;
from practice_one.testCase.ymw_testCase import ymwTestCase;


testunit=unittest.TestSuite();
testunit.addTest(ymwTestCase("test_one"));
unittest.TextTestRunner().run(testunit);


