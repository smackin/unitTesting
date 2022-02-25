""" Example of Unit Tests """
import arithmetic
from unittest import TestCase

class AdderTestCase(TestCase): 
    """examples of unit tests"""
    def test_adder(self):
        assert arithmetic.adder(2,3) == 5
        
    def test_adder_2(self):
        #instead of assert arithmetic.adder(2,2) == 4 ... the below gives a better output in the terminal when you use the built in unit tests.  
        self.assertEqual(arithmetic.adder(2,2), 4)
        

# when running these tests in the terminal,  only the methods with test_ will run as tests.  you can have additional helper methods inside of this class that will not run with the tests.  

# Unit Testing done - via classes.    TestCase is a base class module.   
# 1) define a class that inherits from TestCase 
# 2) methods must begin with test_method  (eg: test_adder)
# 3) to execute the test python -m unittest NAME_OF_FILE will run all test cases.  