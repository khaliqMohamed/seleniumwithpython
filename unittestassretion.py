import unittest

def add_val(a,b):
    return a+b

def diff_val(c,d):
    return c-d

class assertunittest(unittest.TestCase):

    def setUpClass():
        print("class startted")

    def setUp(self):
        self.a=10
        self.b=10
        final_res=add_val(self.a,self.b)
        self.assertEqual(final_res,self.a+self.b)
        print('final value is:',final_res)

    def test_disp(self):
        self.a=20
        self.b=20
        self.assertEqual(self.a,self.b,"same")

    def test_diff(self):
        self.c=40
        self.d=20
        diff_res=diff_res(self.c,self.d)
        

    def tearDown(self):
        self.a=1
        self.b=0
        self.assertTrue(self.a>self.b,"True")
        print('assert finished error or something will be displayed')
    
    def tearDownClass():
        print("class finished")

if __name__=="__main__":
    unittest.main()
        

