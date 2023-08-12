import unittest

class skiptest(unittest.TestCase):
    @unittest.skip("error")
    def test_2(self):
        print("hiiiii")


if __name__=="__main__":
    unittest.main()