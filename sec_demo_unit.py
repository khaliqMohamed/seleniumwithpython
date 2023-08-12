
#import the unittest module
import unittest

#to define some add func for an example


#in unittest class creation is better to define inside a func
class demo_class(unittest.TestCase):

#class paramter---> to invoke the func within the class

    def sum(a,b):
        return a+b

#setup ---> starting point of func and put value of variable one tym and each time if we want to use it
    def setUp(self):
        print("SETUP CALLED.......")
        demo_class.sum.a=10
        demo_class.sum.b=100 

#teardown---> ending point and destroy the value of variable it's not mandatory
    def tearDown(self):
        self.a=0
        self.b=0
        print("TESRDOWN CALLED......")

#to define a func should must be start at the name of test
   
        

    def test_sum_1(self):
        
        print("FUN 2 CALLED.......")
        final_ans=sum(self.demo_class.sum.a,self.demo_class.sum.b)
        self.assertEqual(self.demo_class.sum.a,self.
        demo_class.sum.b,final_ans)
       

    
#main function of unittest invoke the all func and classes
if __name__=="__main__":
    unittest.main() 