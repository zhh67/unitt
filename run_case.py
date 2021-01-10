import unittest
from HTMLTestRunner import HTMLTestRunner

suite=unittest.TestLoader().discover('.idea')
test_report='test_report.html'
with open(test_report,'wb') as f:
    runner=HTMLTestRunner(test_report,title="test_report",description='version1.0')
    runner.run(suite)