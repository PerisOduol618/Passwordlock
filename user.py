import pyperclip
import random
import string


class User:
    '''
    Class User generate a instances of user credentials.
    '''

    user_list = []

    def __init__(self, userName, password):
        '''
        __init__ method that defines the properties for user objects
        '''

        self.userName = userName
        self.password = password

    def save_user(self):
        '''
        user method that saves the objects in the user_list
        '''
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        '''
        method that deletes a saved account from the list
        '''
        User.user_list.remove(self)

class Credentials():
    '''
    class credentials creates new object of creadentials
    '''
    credential_list = []


    def __init__(self, account, userName, email, password):
        '''
        method that defines user credentials
        '''
        self.account = account
        self.userName = userName
        self.email = email
        self.password = password

    def save_credential(self):
        '''
        method that saves the objects in the credential_list
        '''
        Credentials.credential_list.append(self)

    def delete_credential(self):
        '''
        method that deletes an account
        '''
        Credentials.credential_list.remove(self)

   

    @classmethod
    def search_credential(cls, account):
        '''
        Method that takes in a account_name and returns a credential that matches that account_name.

        '''
        for credential in cls.credential_list:
            if credential.account == account:
             return credential

    @classmethod
    def credential_exists(cls, account):
        '''
        Method that checks if a credential exists from the credential list and returns true or false depending on whether the credential exists.
        '''
        for credential in cls.credential_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        '''
        Method that returns all items in the credentials list
        '''
        return cls.credential_list

    # @classmethod
    # def copy_credential(cls, site_name):
    #     '''
    #     Class method that copies a credentials details after the credentials site_name has been entered
    #     '''
    #     find_credential = Credentials.find_by_account(account)
    #     return pyperclip.copy(find_credential.password)

    # @classmethod
    def generate_password(self,stringLength=8):
        '''
        Generate a random password string of letters and digits and special characters
        '''
        password = string.ascii_lowercase + string.ascii_uppercase + "~!@#$%;:^&*"
        return ''.join(random.choice(password) for i in range(int(stringLength)))


    




        
    
     
