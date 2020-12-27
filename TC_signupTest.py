import unittest

class SignupTest(unittest.TestCase):
    def test_signbyemail(self):
        print("This is sign by email test")
        self.assertTrue(True)

    def test_signbyfacebook(self):
        print("This is sign by facebook test")
        self.assertTrue(True)

    def test_signbytwitter(self):
        print("This is sign by twitter test")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()