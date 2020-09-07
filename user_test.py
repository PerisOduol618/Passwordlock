import unittest 
from user import User
from user import Credentials


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
        self.new_user = User("PerisOduol", "oduol254")  # create contact object

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.userName, "PerisOduol")
        self.assertEqual(self.new_user.password, "oduol254")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user()  # saving the new user

    def test_display_user(self):
        '''
        test case to test display user
        '''
        self.new_user.display_user()

    

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a contact from our contact list
        '''
        self.new_user.save_user()
        test_user = User("PerisOduol", "oduol254")  # new user
                               
        test_user.save_user()

        self.new_user.delete_user()  # Deleting a contact object
        self.assertEqual(len(User.user_list), 1)

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases
        '''

        self.new_credential= Credentials("Instagram","dainadee","pepe@gmail.com","pepe123" )
        

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credential_list = []
    

    def test_init(self):
        '''
        Test case to check if a new Credentials instance has been initialized correctly
        '''
        self.assertEqual(self.new_credential.account,"Instagram")
        self.assertEqual(self.new_credential.userName,"dainadee")
        self.assertEqual(self.new_credential.email,"pepe@gmail.com")
        self.assertEqual(self.new_credential.password,"pepe123")



    def test_save_credential(self):
        '''
        test_save_user test case to test if the credential object is saved into the credentials list
        '''
        test_credential = Credentials("instagram", "dainadee","pepe@gmail.com", "pepe123")
        self.new_credential.save_credential()
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list),2)


    def test_delete_credential(self):
        '''
        test method if we can delete an account
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Instagram", "dainadee", "pepe@gmail.com", "pepe123") 
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.credential_list),1)

    # def test_search_credential(self):
    #     '''
    #     test to check is we can search for  a credential  entry by account name and display the details of the credential
    #     '''
    #     self.new_credential.save_credential()
    #     test_credential = Credentials("Instagram","dainadee", "pepe@gmail.com", "pepe123") 
    #     test_credential.save_credential()

    #     find_credential = Credentials.search_credential("instagram")

    #     self.assertEqual(find_credential.account,test_credential.account)
    
    def test_credential_exists(self):
        '''
        Test case to check if a credential exists in the credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Instagram","dainadee", "pepe@gmail.com", "pepe123")
        test_credential.save_credential()

        credential_exists = Credentials.credential_exists("Instagram")
        self.assertTrue(credential_exists)
    
    def test_display_credentials(self):
        '''
        method that returns a list of all the saved credentials
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credential_list)

    def test_generate_password(self):
        '''
        metthod that tests generate password 
        '''
        self.new_credential.generate_password()


if __name__ == '__main__':
    unittest.main()
