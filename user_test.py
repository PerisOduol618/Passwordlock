import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("PerisOduol","oduol254") # create contact object
    
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
         
        self.assertEqual(self.new_user.userName,"PerisOduol")
        self.assertEqual(self.new_user.password,"oduol254")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the contact list
        '''
        self.new_user.save_user() # saving the new user

    
    def test_display_user(self):
        '''
        test case to test display user
        '''
        self.new_user.display_user()
    
if __name__ == '__main__':
    unittest.main()

    