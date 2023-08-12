import unittest

class demotest(unittest.TestCase):
    def setUpClass():
        print("class checked")
    def tearDownClass():
        print("endly checked")

    def setUp(self):
        print("starting at each func.....")

    def tearDown(self):
        print("ending at each func....")

    def test_one(self):
        print("successfully tested_1")

    def test_two(self):
        print("sucessfully tested_2")

if __name__=="__main__":
    unittest.main()