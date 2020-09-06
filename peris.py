import random
import string
import pyperclip
   
class User:
    '''
   Class User Generate a instances of user cridentials.
    '''
    
    users_list = []
    def __init__(self,first_name,last_name,password):
        '''
        __init__ method that defines the properties for user objects 
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.password = password






import unittest
from user import User 

class TestUser(unittest.TestCase):

    # '''
    # Test class that defines test cases for the user class behaviours.

    # Args:
    #     unittest.TestCase: TestCase class that helps in creating test cases
    # '''

    def setup(self):
        #  '''
        #  setup  method to run before each user test cases.
        #  '''
        # # self.new_user =User('Peris', 'Oduol', '0duol254')
        self.user_credential = User("PerisOduol", "Oduol254")

    def test_init(self):
        '''
        test _init test case to check if the object is initialized propeyly
        '''
        
        self.assertEqual(self.user_credential.user_name,"PerisOduol")
        self.assertEqual(self.user_credential.password,"Oduol254")

        
if __name__ == '__main__':
    unittest.main()