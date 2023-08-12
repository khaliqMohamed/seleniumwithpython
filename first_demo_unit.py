
#import the unittest module
import unittest

#to define some add func for an example
def sum(a,b):
    return a+b

#in unittest class creation is better to define inside a func
class demo_class(unittest.TestCase):

#class paramter---> to invoke the func within the class

#setup ---> starting point of func and put value of variable one tym and each time if we want to use it
    def setUp(self):
        print("SETUP CALLED.......")
        self.a=10
        self.b=100 

#teardown---> ending point and destroy the value of variable it's not mandatory
    def tearDown(self):
        self.a=0
        self.b=0
        print("TEARDOWN CALLED......")

#to define a func should must be start at the name of test
    def test_sum(self):
        
        print("FUN 1 CALLED.......")
        final_res=sum(self.a,self.b)
        self.assertEqual(final_res,self.a+self.b)
        

    def test_sum_1(self):
        
        print("FUN 2 CALLED.......")
        result=sum(self.a,self.b)
        self.assertNotEqual(self.a,self.b)
       

    
#main function of unittest invoke the all func and classes
if __name__=="__main__":
    unittest.main() 