import pyperclip
import random
import string


class User:
    '''
    Class User generate a instances of user cridentials.
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

   


