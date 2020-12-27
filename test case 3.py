import unittest


class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("This is login test")

    @classmethod
    def tearDown(self):
        print("This is logout test")

    @classmethod
    def setUpClass(cls):
        print("open applications")

    @classmethod
    def tearDownClass(cls):
        print("close applications")

    def test_search(self):
        print("This is a search test")

    def test_advancedsearch(self):
        print("This is a advancedsearch test")

    def test_prepaidRecharge(self):
        print("This is a prepaid recharge test")

    def test_postpaidRecharge(self):
        print("This is a postpaid Recharge test")

if __name__=="__main__":
    unittest.main()
