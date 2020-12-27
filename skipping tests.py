import unittest

class AppTesting(unittest.TestCase):

    @unittest.SkipTest     #decorator
    def test_search(self):
        print("This is a search test")

    @unittest.skip("I am skipping this test bcoz it is not yet ready")
    def test_advancedsearch(self):
        print("This is a advancedsearch test")

    @unittest.skipIf(1==1,' one is equals to one')
    def test_prepaidRecharge(self):
        print("This is a prepaid recharge test")

    def test_postpaidRecharge(self):
        print("This is a postpaid Recharge test")

    def test_loginbygmail(self):
        print("This is login by email")

    def test_loginbytwitter(self):
        print("This is login by twitter")

if __name__=="__main__":
    unittest.main()